from django.http import JsonResponse


def product(request):

    if request.method == "GET":
        prod = {
                "1": "DEFENSIVOS",
                "2": "SEMENTES",
                "3": "ADUBOS/FERTILIZANTES",
                "5": "SERVICOS",
                "7": "MILHO",
                "8": "SOJA",
                "9": "CORRETIVOS",
                "10": "OUTROS INSUMOS",
                "11": "ORG FEIRA/EXPOSIÇÃO/EVENTOS",
                "50": "IMOBILIZADO",
                "52": "SORGO",
                "53": "MILHETO",
                "54": "MICRONUTRIENTES/ADJUVANTE",
                "55": "INOCULANTES",
                "56": "MATERIAL P/USO E CONSUMO",
                "58": "FEIJAO",
                "59": "GERGELIM",
                "60": "PRODUTOS SHOW AGRO",
                "61": "CONSULTORIA AGRONÔMICA",
                "62": "INSUMOS NUTRIÇÃO ANIMAL CORTE",
                "63": "INSUMOS NUTRIÇÃO ANIMAL LEITE",
                "66": "RAÇÃO PARA NUTRIÇÃO ANIMAL",
                "67": "INSETICIDAS"
            }

    
    return JsonResponse(prod)

def subgroup(request):

    if request.method == "GET":
        sub = {
                "1": {
                    "1": "HERBICIDAS",
                    "2": "INSETICIDAS",
                    "3": "FUNGICIDAS",
                    "4": "INOCULANTES",
                    "21": "TRATAMENTO DE SEMENTES",
                    "22": "ADJUVANTES",
                    "24": "REGULADOR DE CRESCIMENTO",
                    "60": "NEMATICIDAS"
                },
                "2": {
                    "5": "SEMENTE DE SOJA",
                    "6": "SEMENTE DE MILHO",
                    "7": "SEMENTE DE SORGO",
                    "8": "SEMENTE DE FEIJAO",
                    "23": "SEMENTE DE ARROZ",
                    "38": "FORRAGEIRA/PASTAGEM/COBERTURA",
                    "54": "SEMENTE DE MILHETO",
                    "61": "SEMENTE DE GIRASSOL",
                    "63": "SEMENTE DE FEIJÃO",
                    "74": "SEMENTE DE GERGELIM"
                },
                "3": {
                    "9": "FOLIARES/ADUBOS",
                    "19": "FORMULADOS",
                    "20": "ELEMENTOS SIMPLES"
                },
                "5": {
                    "78": "CONSULTORIA AGRONOMICA",
                    "108": "PESQUISA/EXPERIMENTO",
                    "13": "ADQUIRIDOS",
                    "14": "CORRETAGEM",
                    "43": "SERVICOS PRESTADOS",
                    "44": "ENERGIA ELETRICA",
                    "45": "CIP-TAXA DE ILUMINACAO",
                    "46": "JUROS",
                    "58": "ANALISE DE SOLO",
                    "79": "INCENTIVO FORNECEDORES-REBATE",
                    "110": "DIESEL",
                    "111": "COMBUSTIVEL E LUBRIFICANTES",
                    "80": "PESQUISA/EXPERIMENTO",
                    "104": "ABASTECIMENTO MAQUINAS",
                    "105": "ABASTECIMENTO FROTA",
                    "99": "ANALISE DE SEMENTE",
                    "106": "COMBUSTIVEL LUBRIFICANTE"
                },
                "7": {
                    "17": "MILHO EM GRÃOS",
                    "36": "SERVIÇO"
                },
                "8": {
                    "18": "SOJA EM GRÃOS",
                    "37": "SERVIÇO"
                },
                "9": {
                    "39": "CALCARIO",
                    "40": "GESSO",
                    "71": "CÁLCIO"
                },
                "10": {
                    "42": "MERCADORIAS"
                },
                "11": {
                    "117": "CURSOS/TREINAMENTOS"
                },
                "50": {
                    "72": "MAQUINAS/IMPLEMENTOS AGRICOLAS",
                    "73": "MAQUINAS AGRICOLAS",
                    "11": "MAQUINAS E EQUIPAMENTOS",
                    "12": "VEICULOS LEVES",
                    "25": "TERRENOS",
                    "26": "EDIFICAÇÕES",
                    "27": "MOVEIS E UTENSILIOS",
                    "28": "COMPUTADORES E PERIFÉRICOS",
                    "29": "INSTALAÇÕES",
                    "30": "SISTEMA DE SEGURANÇA",
                    "31": "SISTEMA DE COMUNICAÇÃO",
                    "32": "IMPLEMENTOS RODOVIARIOS",
                    "33": "VEICULOS - CAMINHOES",
                    "34": "IMOBILIZADO EM ANDAMENTO",
                    "35": "SOFTWARES",
                    "50": "ATIVO BIOLOGICO",
                    "66": "FERRAMENTAS"
                },
                "52": {
                    "48": "SORGO EM GRÃOS",
                    "49": "SERVIÇO"
                },
                "53": {
                    "51": "MILHETO EM GRÃOS",
                    "57": "SERVIÇO"
                },
                "54": {
                    "52": "FOLIARES/MICRONUTRIENTES",
                    "53": "ADJUVANTES/MICRONUTRIENTES"
                },
                "55": {
                    "59": "INOCULATES"
                },
                "56": {
                    "113": "MANUTENÇÃO CORRETIVA",
                    "109": "DIESEL",
                    "114": "SANDUICHEIRA"
                },
                "58": {
                    "68": "SERVIÇOS",
                    "67": "FEIJAO EM GRAOS"
                },
                "59": {
                    "69": "GERGELIM EM GRAOS",
                    "70": "SERVICO"
                },
                "60": {
                    "75": "BONECO DIVERSOS",
                    "76": "ACESSORIOS"
                },
                "61": {
                    "77": "SERVIÇOS DE CONSULTORIA"
                },
                "62": {
                    "90": "NUCLEOS",
                    "88": "SAL MINERAL",
                    "89": "SAL MINERAL PROTEINADO",
                    "91": "PROTEINADO",
                    "92": "MUB",
                    "87": "RAÇÃO"
                },
                "63": {
                    "93": "RAÇÃO",
                    "94": "SAL MINERAL",
                    "95": "SAL MINERAL PROTEINADO",
                    "96": "NUCLEOS",
                    "97": "PROTEINADO"
                },
                "66": {
                    "102": "FARELO DE SOJA",
                    "103": "TORTA DE SOJA"
                },
                "67": {
                    "107": "INSECTO"
                }
            }

    return JsonResponse(sub)
