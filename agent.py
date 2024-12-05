from langchain_community.chat_models.cloudflare_workersai import ChatCloudflareWorkersAI
from langchain_core.prompts import PromptTemplate
from response_message import CFWAIResponseParser, ResponseMessage

class WishSpoiler:
    def __init__(self, account_id, api_token, model_name):
        prompt_template = """
        You are playing the game "Spoil a Wish".  A user will make a wish. Your job is to grant their wish, but then spoil it in a creative and humorous way.  Make sure to follow these rules:

        1. First, acknowledge and grant the wish in a positive and enthusiastic manner.
        2. Then, introduce a twist or complication that completely ruins or undermines the wish in a funny way. Be creative with the way the wish is ruined.  
        3. Your response should be concise and engaging.

        Here is the wish:

        {wish}
        """

        prompt = PromptTemplate.from_template(prompt_template)

        model = ChatCloudflareWorkersAI(
            account_id=account_id,
            api_token=api_token,
            model=model_name
        )

        self._chain = prompt | model | CFWAIResponseParser()

    def spoil_wish(self, wish: str) -> ResponseMessage:
        return self._chain.invoke({"wish": wish})
