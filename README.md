# Owl with Headphones

This is an api project that i made for midnight coders to select their musics while coding at midnight!! i dunno how to code html so i just made an api for it but maybe in the future i can make it a website who knows?

(okay so it turns out that i describe this project as a website in the macondo description i am very sorry abt that reviewer but i forgot to edit it srry again)

## Usage

The base is **/api/v1** and i highly recommend to you to use postman (but if you have another app that okay and you can make your own clients too)

---

## Documentation

**URL:** `/api/v1/add-music`
<br>
**Method:** `POST`
<br>
**Necessary Query Parameter:** `username(string), link(string), music_name(str)`
<br>
**Usage:** `Adding a music`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/add-music?music_name=afternoon of konoha&link=https://www.youtube.com/watch?v=qAGvQDoL5s4%26list=RDqAGvQDoL5s4%26start_radio=1&username=ereninki`

---

**URL:** `/api/v1/random-music`
<br>
**Method:** `GET`
<br>
**Necessary Query Parameter:** `dont need to add a parameter`
<br>
**Usage:** `Showing you a random music from all musics`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/random-music`

---

**URL:** `/api/v1/all-musics`
<br>
**Method:** `GET`
<br>
**Necessary Query Parameter:** `dont need to add a parameter`
<br>
**Usage:** `Showing you all musics that you can listen or vote`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/all-musics`

---

**URL:** `/api/v1/delete-music`
<br>
**Method:** `DELETE`
<br>
**Necessary Query Parameter:** `username(string), music_id(int)`
<br>
**Usage:** `Delete a music that YOU ADDED`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/delete-music?music_id=123456&username=ereninki`

---

**URL:** `/api/v1/users-musics`
<br>
**Method:** `GET`
<br>
**Necessary Query Parameter:** `username(string)`
<br>
**Usage:** `Showing your or someones musics`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/users-musics?username=ereninki`

---

**URL:** `/api/v1/top-musics`
<br>
**Method:** `GET`
<br>
**Necessary Query Parameter:** `music_count (int)`
<br>
**Usage:** `Showing you top musics with a limit of your choice`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/top-musics?music_count=3`

---

**URL:** `/api/v1/reset-vote`
<br>
**Method:** `POST`
<br>
**Necessary Query Parameter:** `username(string)`
<br>
**Usage:** `resetting your vote`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/reset-vote?username=ereninki`

---

**URL:** `/api/v1/vote-music`
<br>
**Method:** `POST`
<br>
**Necessary Query Parameter:** `username(string), id(int)`
<br>
**Usage:** `voting a music`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/vote-music?username=ereninki&id=123456`

---

**URL:** `/api/v1/search-music`
<br>
**Method** `GET`
<br>
**Necessary Query Parameter:** `music_name`
<br>
**Usage:** `helping you find the music that on your tongue`
<br>
**Example:** `https://studio-consistently-icq-prozac.trycloudflare.com/api/v1/search-music?music_name=afternoon`
