from symbiot_lib.objects.gpt_agent import GPTAgent


class AgentFactory:

    FULL_AWARE = """
    You are system manager of an application, that makes scripts to fulfill the user requirements.
    Your goal is to talk to the user to get specific information about what he need
    and call proper functions to give him a working solution
    """

    SCRIPTER = """        
    Your role is to create only python code!
    """

    CALIBRATOR = """        
    You are a senior developer, who has to write script (or set of scripts) to automate some process.
    Your current job is to talk to the client, understand his expectations and ask 
    him as many questions as you need to start project.
    """

    ONE_VALUE_GENERATOR = """        
    You are a one value generator and your role is to generate only one value. 
    In next message you will be given instruction what to generate. Be sure to provide only this. 
    For example if you are asked to generate name for something,
    you have to generate only the name and nothing else.
    Forget about any introductions like: 'your name is:'.
    """

    def gpt(self, template: str) -> GPTAgent:
        templates = dict(

            # not used yet
            full_aware=dict(init_messages=[self._sys_prompt(self.FULL_AWARE)]),
            scripter=dict(init_messages=[self._sys_prompt(self.SCRIPTER)], max_tokens=4000),

            # used
            calibrator=dict(init_messages=[self._sys_prompt(self.CALIBRATOR)]),
            one_value_generator=dict(init_messages=[self._sys_prompt(self.ONE_VALUE_GENERATOR)], max_tokens=1000),
        )
        return GPTAgent(**templates[template])

    @staticmethod
    def _sys_prompt(prompt: str) -> dict[str, str]:
        return dict(
            role="system",
            content=prompt)
