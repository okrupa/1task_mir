delivery_company_ = ['delivery_company_360.0','delivery_company_516.0','delivery_company_620.0']
delivery_company_number = [360,516,620]
    
def get_delivery_company(delivery_company):
    d_company = {}
    for i in delivery_company_:
        d_company[i] = 0
    if delivery_company in delivery_company_number:
        name = 'delivery_company_'+ str(float(delivery_company))
        d_company[name] = 1
    return d_company