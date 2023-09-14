import openai


class GPTConnector:
    def __init__(self):
        self.output = ""
        self.history = {}

    @staticmethod
    def set_api_key(api_key):
        openai.api_key = api_key

    def gpt_text_davinci_003p1(self, prompt):

        prompt = prompt
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.1,
            max_tokens=3400)

        output = response.choices[0].text

        self.output = output

        # output_history[len(output_history)+1] = output

        return output

    def gpt_text_davinci_003p2(self, prompt):

        prompt = self.output + ' ' + prompt
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.1,
            max_tokens=3000)

        output = response.choices[0].text

        # zapisanie wartości do zmiennej globalnej
        self.output = output

        return output

    def respond(self, prompt):
        # global output_history
        print("respond")
        prompt = prompt
        if len(self.output) == 0:
            p = self.gpt_text_davinci_003p1(prompt)
        else:
            p = self.gpt_text_davinci_003p2(prompt)

        self.history[-1] = p
        return p
