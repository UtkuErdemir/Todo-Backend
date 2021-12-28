from pact.verifier import Verifier


def todo_service_provider_against_pact():
    verifier = Verifier(provider='todo-app-provider', provider_base_url="http://localhost:5000")
    output, logs = verifier.verify_pacts('./pacts/todo-app-consumer-todo-app-provider.json')
    print(output)
    assert output == 0
