from fastapi import Header, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from random import randint

"""i dunno why but i love writing api project and still dunno how to use them in site (i dunno how to use html tbh😭)"""

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

async def read_musics():
    try:
        with open("musics.json", "r", encoding="utf-8") as file:
            musics = json.load(file)
            return musics
    except Exception as e:
        print(f"wth is this error {e}")

async def write_musics(musics):
    try:
        with open("musics.json", "w", encoding="utf-8") as file:
            musics = json.dump(musics, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"where did my pencil go? {e}")

allowed_domains = ["youtube.com", "youtu.be", "spotify.com", "open.spotify.com", "soundcloud.com", "music.youtube.com"]

@app.post("/api/v1/add-music")
async def add_music(music_name: str, link: str, username: str):
    if not link.startswith("www.") and not link.startswith("https://"):
        raise HTTPException(400, "the link must be start with www. or https:// pls do not put a virus link inside")
    
    musics = await read_musics()
    
    valid = False
    for a in allowed_domains:
        if a in link:
            valid = True
            break

    if not valid:
        raise HTTPException(400, "the link must be a youtube spotify yt music or a soundcloud link idc if its apple music or another music platform")

    for a in musics["musics"]:
        if a == music_name:
            raise HTTPException(400, "this music name is already added bruh, pls check '/api/v1/all-musics' before adding a music")

    for a in musics["musics"]:
        if link == musics["musics"][a]["link"] or link in musics["musics"][a]["link"]:
            raise HTTPException(400, "this link is already added bruh, pls check '/api/v1/all-musics' before adding a music")

    all_music_ids = []
    id = randint(0,99999)
    for music in musics["musics"]:
        all_music_ids.append(musics["musics"][music]["id"])
    while(True):
        if id in all_music_ids:
            id = randint(0,99999)
        else: 
            break

    musics["musics"][music_name] = {"id": id, "vote": 0, "link": link, "added_by": username, "voted_by": []}
    await write_musics(musics)
    return {"success": "your music is successfully added to the database!!!"}

@app.get("/api/v1/random-music")
async def get_random_music():
    musics = await read_musics()
    
    music_names = []
    for a in musics["musics"]:
        music_names.append(a)

    random_music_number = randint(0, len(music_names)-1)
    random_music = musics["musics"][music_names[random_music_number]]
    return {"message": "here's your music!!! (hope youll like it)", str(music_names[random_music_number]): random_music}

@app.get("/api/v1/all-musics")
async def get_all_musics():
    musics = await read_musics()
    all_musics = {}
    for music in musics["musics"]:
        all_musics[music] = {"id": musics["musics"][music]["id"], "link": musics["musics"][music]["link"], "vote": musics["musics"][music]["vote"], "added_by": musics["musics"][music]["added_by"]}
    return {"musics": all_musics}

@app.delete("/api/v1/delete-music")
async def delete_music(username: str, music_id: int):
    musics = await read_musics()
    
    is_id_valid = False
    can_user_delete_this = False
    for a in musics["musics"]:
        if music_id == musics["musics"][a]["id"]:
            is_id_valid = True
            if username == musics["musics"][a]["added_by"]:
                can_user_delete_this = True
                the_music_that_will_deleted = a
            break
    
    if is_id_valid == False:
        raise HTTPException(400, "bruh, are you trying to delete the nothingness?? pls dont do this here and pls check the '/api/v1/users-musics' for finding a music that you added")
    if can_user_delete_this == False:
        raise HTTPException(403, "bro why are you trying to delete a music that isnt yours this is disrespectfull af pls check '/api/v1/users-musics' for musics that you want to delete")

    del musics["musics"][the_music_that_will_deleted]
    await write_musics(musics)
    return {"success": "your music is successfully deletedd!1111!!1111!!11!!!1!!!!!"}

@app.get("/api/v1/users-musics")
async def get_users_musics(username: str):
    musics = await read_musics()
    users_musics = {}
    for a in musics["musics"]:
        if username == musics["musics"][a]["added_by"]:
            users_musics[a] = {"id": musics["musics"][a]["id"], "vote": musics["musics"][a]["vote"], "link": musics["musics"][a]["link"]}

    if users_musics == {}:
        raise HTTPException(404, "bruh are you trying to see the nothingness or smth bc you didnt even add a single music.. GO AND ADD A MUSIC FIRST")

    return {"musics": users_musics}

@app.get("/api/v1/top-musics")
async def get_top_musics(music_count: int):
    musics = await read_musics()

    if len(musics["musics"]) < music_count:
        raise HTTPException(400, "srry bro but you enter a number that bigger then the total music count 💀 pls insert a smaller number (0 for all musics)")
    
    if music_count < 0:
        raise HTTPException(400, "bruh, there is no negative musics if you want it then go to the apple music they have trash there but not here")

    if music_count == 0:
        music_count = len(musics["musics"])

    musics_but_sorted = sorted(
        musics["musics"].items(),
        key=lambda music_vote: music_vote[1]["vote"],
        reverse=True
    )

    musics_but_only_music_counts = musics_but_sorted[:music_count]

    musics_but_ordered = {}
    for a, b in musics_but_only_music_counts:
        musics_but_ordered[a] = {"id": b["id"], "vote": b["vote"], "link": b["link"], "added_by": b["added_by"]}

    return{"musics": musics_but_ordered}

@app.post("/api/v1/reset-vote")
async def reset_vote(username: str):
    musics = await read_musics()

    is_user_voted = False
    for a in musics["musics"]:
        if username in musics["musics"][a]["voted_by"]:
            is_user_voted = True
            musics["musics"][a]["voted_by"].remove(username)
            musics["musics"][a]["vote"] -= 1
            break

    if is_user_voted == False:
        raise HTTPException(400, "bruh, you can vote you know? bc you didnt even vote yet pls go and vote before resetting your vote")
    
    await write_musics(musics)
    return {"success": "your vote is succesfully removed!11111!!!111!!1!"}

@app.get("/api/v1/search-music")
async def search_music(music_name: str):
    musics = await read_musics()
    possible_musics = []

    if music_name.strip() == "":
        raise HTTPException(400, "pls put a music name, not my brain")

    for a in musics["musics"]:
        if music_name.lower() in a.lower():
            possible_musics.append(a)

    if possible_musics == []:
        return {"message": "sorry bro but there is no music with that name, maybe you can check '/api/v1/all-musics' to see all the musics"}

    return {"did you mean": possible_musics}

@app.post("/api/v1/vote-music")
async def vote_music(id: int, username: str):
    musics = await read_musics()

    is_id_valid = False
    is_user_can = True

    for a in musics["musics"]:
        if username in musics["musics"][a]["voted_by"]:
            is_user_can = False
            break
    
    if not is_user_can:
        raise HTTPException(400, "bruh, you already voted a music pls go to the '/api/v1/reset-vote' for resetting your vote")

    for a in musics["musics"]:
        if musics["musics"][a]["id"] == id:
            musics["musics"][a]["vote"] += 1
            musics["musics"][a]["voted_by"].append(username)
            is_id_valid = True
            await write_musics(musics)
            break

    if is_id_valid == False:
        raise HTTPException(400, "bruh, there is no music with this id pls check '/api/v1/all-musics' to check the id fro your music")
    else:
        return {"success": "succesfully voted for that music!!!11!111!1!!1 (i dunno what music it is but im sure its a w/ music)"}
    
@app.get("/api/v1")
async def health():
    return {"health": "OK"}
    

if __name__ == "__main__":
    uvicorn.run(app)