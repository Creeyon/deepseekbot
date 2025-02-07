from services.deepseek_api import get_deepseek_response
import utils.__init__ as utils

async def ask_deepseek(ctx, *, question: str):
    response = get_deepseek_response(question)
    await ctx.send(utils.format_response(response))
    utils.log_message(response)