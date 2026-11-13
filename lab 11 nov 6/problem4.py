# Problem 4: LLM and AICompany classes

# Part (a): LLM class
class LLM:
    def __init__(self, name, token_limit):
        self.name = name
        self.token_limit = token_limit

    def get_token_limit(self):
        return self.token_limit

    def set_token_limit(self, token_limit):
        self.token_limit = token_limit

    def __str__(self):
        return f"LLM(name={self.name}, token_limit={self.token_limit})"


# Part (b): AICompany class
class AICompany:
    def __init__(self, company_name, founding_year, headquarters):
        self.company_name = company_name
        self.founding_year = founding_year
        self.headquarters = headquarters
        self.llms = []

    def get_headquarters(self):
        return self.headquarters

    def set_headquarters(self, headquarters):
        self.headquarters = headquarters

    def add_llm(self, llm):
        self.llms.append(llm)

    def display_models(self):
        if not self.llms:
            print(f"{self.company_name} has no LLMs yet.")
        else:
            print(f"{self.company_name} LLMs:")
            for llm in self.llms:
                print(f" - {llm.name} ({llm.token_limit} tokens)")

    def __str__(self):
        return f"AICompany(name={self.company_name}, founded={self.founding_year}, headquarters={self.headquarters})"


# Part (c): Demonstration
if __name__ == "__main__":
    company = AICompany("OpenMind", 2020, "Seattle")
    llm1 = LLM("Nova", 128000)
    llm2 = LLM("Atlas", 256000)

    company.add_llm(llm1)
    company.add_llm(llm2)

    print(company)
    print(llm1)
    print(llm2)
    company.display_models()
