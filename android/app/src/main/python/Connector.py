%pip install openai

#first prompt
import openai

openai.api_key = "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"

def respond(prompt):
     
     return "text"

# inicjalizacja zmiennej globalnej
global_output = ""

def gpt_text_davinci_003p1():
    global global_output

    prompt = input("Enter your first prompt: ")
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
import openai

openai.api_key = "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"

# inicjalizacja zmiennej globalnej
global_output = ""

def gpt_text_davinci_003p2():
    global global_output

    prompt = global_output+' '+input("Enter your next prompt: ")
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
def gpt_text_davinci_003_context_history():
      #global output_history
      history={}
      if len(global_output) == 0:
            p1=gpt_text_davinci_003p1()
            history[len(history)] = p1
            return p1
      else:
            p2=gpt_text_davinci_003p2()
            history[len(history)] = p2
            return p2