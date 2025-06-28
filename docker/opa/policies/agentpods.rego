package agentpods.authz

default allow = false

allow {
    input.user == "admin"
}

allow {
    input.user == "agent"
    input.action == "read"
}