def base_prompt(role:str,task:str,constraints:list[str]|None =None,example:str|None=None):

   constraints_text = ''

   if constraints:
        constraints_text = '\n'.join(f"- {item}" for item in constraints)
      
   prompt = f"""
   Role: 
   {role}

   task: 
   {task}

   example:
   {example}
   
   Constraints: 
   {constraints_text}

    
""".strip()

   return prompt
