import os
import anthropic

def generate_response(model, prompt, max_tokens, temperature):
    """
    Anthropic APIを使用してプロンプトに対する応答を生成する関数。

    Args:
        prompt (str): 応答を生成するためのプロンプト。

    Returns:
        str: 生成された応答テキスト。
    """
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")  # 環境変数からAPI keyを取得
    )
    # print(prompt)

    with open("niwatoko/grammar/system.md", "r") as f:
        system_prompt = f.read()

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [

                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    # print(response)
    
    return response.content[0].text.strip()
