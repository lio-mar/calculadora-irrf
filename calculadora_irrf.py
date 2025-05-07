class CalculadoraINSS:
    """
    Classe para calcular o desconto de INSS (conforme aula do dia 12/04)
    """
    @staticmethod
    def calcular_inss(salario_bruto):
        if salario_bruto <= 1412.00:
            return salario_bruto * 0.075
        elif 1412.01 <= salario_bruto <= 2666.68:
            return (1412.00 * 0.075) + ((salario_bruto - 1412.00) * 0.09)
        elif 2666.69 <= salario_bruto <= 4000.03:
            return (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((salario_bruto - 2666.68) * 0.12)
        elif 4000.04 <= salario_bruto <= 7786.02:
            return (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((salario_bruto - 4000.03) * 0.14)
        else:
            return 7786.02 * 0.14

class CalculadoraIRRF:
    """
    Classe para calcular o desconto de IRRF
    """
    @staticmethod
    def calcular_irrf(salario_bruto):
        # Primeiro calcula o INSS
        inss = CalculadoraINSS.calcular_inss(salario_bruto)
        
        # Calcula o salário base (salário bruto - INSS)
        salario_base = salario_bruto - inss
        
        # Tabela IRRF 2023 (valores podem ser atualizados conforme necessário)
        faixas_irrf = [
            {"min": 0, "max": 2112.00, "aliquota": 0, "deducao": 0},
            {"min": 2112.01, "max": 2826.65, "aliquota": 0.075, "deducao": 158.40},
            {"min": 2826.66, "max": 3751.05, "aliquota": 0.15, "deducao": 370.40},
            {"min": 3751.06, "max": 4664.68, "aliquota": 0.225, "deducao": 651.73},
            {"min": 4664.69, "max": float('inf'), "aliquota": 0.275, "deducao": 884.96}
        ]
        
        # Encontra a faixa correspondente
        for faixa in faixas_irrf:
            if faixa["min"] <= salario_base <= faixa["max"]:
                irrf = (salario_base * faixa["aliquota"]) - faixa["deducao"]
                return max(irrf, 0)  # Não retorna valor negativo
        
        return 0

# Exemplo de uso
if __name__ == "__main__":
    salario_bruto = 3000.00
    inss = CalculadoraINSS.calcular_inss(salario_bruto)
    irrf = CalculadoraIRRF.calcular_irrf(salario_bruto)
    
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Salário Base: R$ {salario_bruto - inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
