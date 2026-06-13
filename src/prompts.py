def build_customer_support_prompt(instruction: str) -> str:
    """
    Prompt for customer support response generation, to be used across all evaluation axes. 
    The prompt instructs the model to act as a professional customer support agent and 
    provides the customer's question or request. 
    
    Args:
        instruction: The customer question or request string

    Returns:
        Formatted prompt string ready for model inference
    """
    return (
        f"You are a professional customer support agent. "
        f"Answer the following customer question clearly and helpfully.\n\n"
        f"Customer: {instruction}\n\n"
        f"Agent:"
    )