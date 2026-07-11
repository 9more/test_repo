from class_files import Main

path= Main.get_data()

df=Main.load(path)

text=Main.extract(df)

print('trainging starts')

model, Xtest, ytest = Main.model_train(text)

model_eval = Main.model_eval(model, Xtest, ytest)
print('F1 score:', model_eval)

Main.model_dump(model, 'saved_model')