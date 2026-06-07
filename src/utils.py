from pickle import load

def load_model(path):
    model = load(open(path, "rb"))
    return model

def make_forecast(model, steps):
    forecast = model.forecast(steps)
    
    dates = forecast.index.strftime("%Y-%m-%d").tolist()
    values = [round(v, 2) for v in forecast.values.tolist()]
    
    return list(zip(dates, values))