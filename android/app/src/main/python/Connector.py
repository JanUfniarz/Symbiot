
#first prompt
import openai

openai.api_key = "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"
'''
def respond(prompt):
    prompt=prompt
    x=gpt_text_davinci_003p1(prompt)
    return x
'''
# inicjalizacja zmiennej globalnej
global_output = ""

def gpt_text_davinci_003p1(prompt):
    global global_output

    prompt = prompt
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.1,
        max_tokens=3400)

    output=response.choices[0].text

    # zapisanie wartości do zmiennej globalnej
    global_output = output

    #output_history[len(output_history)+1] = output

    return output

#next prompt



# inicjalizacja zmiennej globalnej
global_output = ""

def gpt_text_davinci_003p2(prompt):
    global global_output

    prompt = global_output+' '+prompt
    print(prompt)
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.1,
        max_tokens=3000)

    output=response.choices[0].text

    # zapisanie wartości do zmiennej globalnej
    global_output = output

    return output

#sukces
def respond(prompt):
    '''
      prompt=prompt
      global output_history
      history={}
      if len(global_output) == 0:
            p1=gpt_text_davinci_003p1(prompt)
            history[len(history)] = p1
            return p1
      else:
            p2=gpt_text_davinci_003p2(prompt)
            history[len(history)] = p2
            return p2
    '''

    return prompt