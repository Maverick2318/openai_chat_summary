import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """Summarize this incident chat transcript [Person 1] Hi, we've been seeing reports of down time in our Europe region. Can anyone check?

[Person 2] Yes, I'm on it.

[Person 3] I'm also looking into it.

[Person 4] I can look into this too.

[Person 5] I just ran a diagnostic on our servers and everything looks good from here.

[Person 6] I'm checking the databases now.

[Person 7] We'll need to talk to the hosting provider to get more information about what's going on.

[Person 8] I just checked with our server engineers and they said that the issue appears to be related to the DNS servers. They are working on resolving the issue now.

[Person 1] Thanks everyone for all your help. We'll keep monitoring the situation and inform everyone if anything changes."""

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  temperature=0.4,
  max_tokens=64
)

print (response)
