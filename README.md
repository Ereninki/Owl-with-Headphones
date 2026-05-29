# Owl with Headphones

This is an api project that i made for midnight coders to select their musics while coding at midnight!! i dunno how to code html so i just made an api for it but maybe in the future i can make it a website who knows?

## Usage

The base is **/api/v1** and i highly recommend to you to use postman (but if you have another app that okay and you can make your own clients too)

---

## Documentation

**URL:** `/api/v1/add-music`
**Method:** `POST`
**Necessary Query Parameter:** `username(string), link(string), music_name(str)`
**Usage:** `Adding a music`
**Example:** `https://personals-point-difficulties-hunt.trycloudflare.com/api/v1/add-music?music_name=afternoon of konoha&link=https://www.youtube.com/watch?v=qAGvQDoL5s4%26list=RDqAGvQDoL5s4%26start_radio=1&username=ereninki`

---

**URL:** `/api/v1/random-music`
**Method:** `GET`
**Necessary Query Parameter:** `dont need to add a parameter`
**Usage:** `Showing you a random music from all musics`
**Example:** `https://personals-point-difficulties-hunt.trycloudflare.com/api/v1/random-music`

---

**URL:** `/api/v1/all-musics`
**Method:** `GET`
**Necessary Query Parameter:** `dont need to add a parameter`
**Usage:** `Showing you all musics that you can listen or vote`
**Example:** `https://personals-point-difficulties-hunt.trycloudflare.com/api/v1/all-musics`

---

**URL:** `/api/v1/delete-music`
**Method:** `DELETE`
**Necessary Query Parameter:** `username(string), music_id(int)`
**Usage:** `Delete a music that YOU ADDED`
**Example:** `https://personals-point-difficulties-hunt.trycloudflare.com/api/v1/delete-music?music_id=123456&username=ereninki`

---

**URL:** `/api/v1/users-musics`
**Method:** `GET`
**Necessary Query Parameter:** `username(string)`
**Usage:** `Showing your or someones musics`
**Example:** `https://personals-point-difficulties-hunt.trycloudflare.com/api/v1/users-musics?username=ereninki`

---

**URL:** `/api/v1/top-musics`
**Method:** `GET`
**Necessary Query Parameter:** `music_count (int)`
**Usage:** `Showing you top musics with a limit of your choice`
**Example:** `https://personals-point-difficulties-hunt.trycloudflare.com/api/v1/top-musics?music_count=3`

---

**URL:** `/api/v1/reset-vote`
**Method:** `POST`
**Necessary Query Parameter:** `username(string)`
**Usage:** `resetting your vote`
**Example:** `https://personals-point-difficulties-hunt.trycloudflare.com/api/v1/reset-vote?username=ereninki`

---

**URL:** `/api/v1/vote-music`
**Method:** `POST`
**Necessary Query Parameter:** `username(string), id(int)`
**Usage:** `voting a music`
**Example:** `https://personals-point-difficulties-hunt.trycloudflare.com/api/v1/vote-music?username?=ereninki&id=123456`