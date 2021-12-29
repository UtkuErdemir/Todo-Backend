from pact.verifier import Verifier

verifier = Verifier(provider='todo-app-provider', provider_base_url="http://localhost:5000")
output, logs = verifier.verify_pacts('./pacts/todo-app-consumer-todo-app-provider.json')
assert output == 0
