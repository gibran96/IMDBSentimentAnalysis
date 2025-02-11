from data_processing import l1_norm, l2_norm, load_data
from data_processing import pad_data
from model_architecture import create_model
from model_architecture import set_callbacks
from matplotlib import pyplot as plt

def train_model():
    XT, YT, Xt, Yt = load_data()
    XT, Xt = pad_data(XT, Xt)
    model = create_model()
    callbacks = set_callbacks()
    hist = model.fit(XT, YT, validation_split=0.2, epochs=20, batch_size=128) 
    return hist, model, Xt, Yt

def plot_graphs(hist):
    acc = hist.history['acc']
    val_acc = hist.history['val_acc']
    loss = hist.history['loss']
    epochs = range(1,len(loss)+1)

    plt.title("Accuracy vs Epochs")
    plt.plot(epochs,acc,label="Training Acc")
    plt.plot(epochs,val_acc,label="Val Acc")
    plt.legend()
    plt.savefig("Accuracy_8.png")

    plt.close()

    loss = hist.history['loss']
    val_loss = hist.history['val_loss']

    epochs = range(1,len(loss)+1)

    plt.title("Loss vs Epochs")
    plt.plot(epochs,loss,label="Training Loss")
    plt.plot(epochs,val_loss,label="Val Loss")
    plt.legend()
    plt.savefig("Loss_8.png")

def evaluate_model(model,Xt,Yt):
    print("Evaluating Model")
    print(model.evaluate(Xt,Yt))

if __name__ == '__main__':
    hist, model, Xt, Yt = train_model()
    plot_graphs(hist)
    model.save("models/model50_8.keras")
    evaluate_model(model,Xt,Yt)


