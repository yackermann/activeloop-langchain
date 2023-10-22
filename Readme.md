ActiveLoop Langchain Course Files
===

My files for activeloop course https://learn.activeloop.ai/courses/take/langchain/multimedia/46318189-introduction-to-llm-memory

This is a fantastic course and I highly recommend it for anyone to try it. It is free and you can get a lot of value from it.

Big big :love: to the ActiveLoop team for making this course!

PS. Starting from S5 it uses ChromaDB instead of activeloop


# Dev

- Install deps `pip install -r requirements.txt`
- Rename `example.env` to `.env` and fill in the values. See below for more info


# Getting access tokens:

### OpenAI:

 - Register with OpenAI: https://openai.com/
 - Go to API keys tab: https://platform.openai.com/account/api-keys
 - Create new API key
 - Set `OPENAI_KEY` env variable in the `.env`

### ActiveLoop:

 - Register with ActiveLoop https://www.activeloop.ai/
 - `Create API Token` -> `Create API Token`
 - Set `ACTIVELOOP_TOKEN` and `ACTIVELOOP_ORGID` env variable in the `.env`


### Google Application Credentials

 - Install Google Cloud CLI https://cloud.google.com/sdk/docs/install
 - Run `gcloud auth application-default login` to authenticate
 - Set `GOOGLE_APPLICATION_CREDENTIALS` to the location of your app credentials
  + `Linux, macOS: $HOME/.config/gcloud/application_default_credentials.json`
  + `Windows: %APPDATA%\gcloud\application_default_credentials.json`
  + https://cloud.google.com/docs/authentication/application-default-credentials


### Google Custom Search Engine

 - Login to your Google account. 
 - Create custom search engine https://programmablesearchengine.google.com/controlpanel/create
 - Select "Search Entire Web" and click "Create"
 - Once its created press "Customise" and copy the "Search engine ID" from the top of the page. Thats is the `GOOGLE_CSE_ID` var
 - Go to https://developers.google.com/custom-search/v1/introduction and press "Get A Key" blue button to get the `GOOGLE_API_KEY`.

### Eleven Labs

 - Create account with ElevenLabs https://elevenlabs.io/
 - Once you logged in, press on your account icon, and select "Profile"
 - You will see the "API Key" there. Thats is the `ELEVENLABS_API_KEY` var


### SerpAPI

 - Create account with SerpAPI https://serpapi.com/
 - This will require both `email` and `phone` verification. (YES THEY WILL ASK FOR YOUR PHONE NUMBER)
 - Go to the API keys dashboard https://serpapi.com/manage-api-key
 - You will see the key there. Thats is the `SERPAPI_API_KEY` var
 
### WolframAlpha

 - Create developer account with WolframAlpha https://developer.wolframalpha.com/
 - Once you signed in, press "Get an App ID" button
 - Fill in name, and description.
 - In the `API` selector choose `Simple API` and press submit
- You will see the `App ID` there. Thats is the `WOLFRAM_ALPHA_APPID` var