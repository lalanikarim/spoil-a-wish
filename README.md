---
title: Spoil A Wish
emoji: 🔥
colorFrom: yellow
colorTo: yellow
sdk: gradio
sdk_version: 5.8.0
app_file: app.py
pinned: false
license: mit
short_description: Spoil-A-Wish
---

# Spoil-A-Wish with LangChain, Cloudflare Workers AI, and Gradio

Spoil-A-Wish is a fun little game you play with friends where you make a wish and your friend grants it with a twist, essentially ruining it.

For example:

```
Wish: I wish for a million dollars.  
Response: Granted, but you get a million dollars in ZWL (Zimbabwe's defunct currency) which equals $15 USD. Enjoy your happy meal.
```

In this sample project, we will create a simple AI Agent that spoils your wishes.

We will build it with [LangChain](https://www.langchain.com) using [llama 3.1 70b instruct](https://developers.cloudflare.com/workers-ai/models/llama-3.1-70b-instruct/) model hosted on [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/).  

`llama 3.1 70b instruct` model is available for free by Cloudflare while it is still in `beta` status. Other models are also available with [daily free token allocations](https://developers.cloudflare.com/workers-ai/platform/pricing/#free-allocation).

You will need your Cloudflare Account ID and API Token for this exercise.  
You can register for a free Cloudflare Account [https://www.cloudflare.com/](https://www.cloudflare.com/).

Account ID can be found at [https://dash.cloudflare.com](https://dash.cloudflare.com) under the `Overview` section towards the bottom. You may have to select a domain if you have multiple domains on your account.

API Token can be created [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens). Make sure to give it permissions for `Workers AI`.

List of all availabe models supported by `Cloudflare Workers AI` can be found at [https://developers.cloudflare.com/workers-ai/models/](https://developers.cloudflare.com/workers-ai/models/).  
Select `Text Generation` under `Model Types`.