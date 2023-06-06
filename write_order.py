import json
import spacy
import numpy as np
from numpy.linalg import norm
from sklearn.metrics.pairwise import cosine_similarity
from spacy.training.example import Example

# Load W2V
def load_mappings(dataset):
    f = open(dataset, 'r',encoding='utf-8')
    model= dict({})
    for line in f:
        tem=line.split()
        vtem=[]
        for i in range(1,len(tem)):
            vtem.append( float(tem[i].strip()))
        vec1=np.array(vtem)
        model.update({tem[0].strip():vec1})
    return model

def train (label, train_data, model):
    # Add the new label to the entity recognizer
    # Load the pre-trained model
    nlp = spacy.load(model)

    nlp_train = spacy.load(model)

    ner = nlp_train.get_pipe("ner")
    ner.add_label(label)

    # Fine-tune the model
    optimizer = nlp_train.resume_training()
    for i in range(10):
        for example in train_data:
            doc = nlp_train(example[0])
            gold = Example.from_dict(doc, example[1])
            nlp_train.update([gold], sgd=optimizer)
    return nlp_train

def get_product(text : str, train_model) -> str :
    # Test the model train
    list_test = []
#     label = ["PRODUCT","PRICE"]
    doc = train_model(text)        
    for ent in doc.ents:
        #if ent.label_ in label:
        list_test.append([ent.text, ent.label_])
    return list_test

# get_product_category 
def get_product_category(my_product, my_list):
    for i in my_product:
        if i[1] == "PRODUCT":
            product = i[0]
    if product in load_model: 
        embeddings = []
        v1 = load_model[product.strip()]
        embeddings.append(v1)
        for category in my_list:
            embeddings.append(load_model[category.strip()])
        cos_sim = cosine_similarity( [embeddings[0]], embeddings[1:])
        return my_list[np.argmax(cos_sim)]
    return 0

def Workflow(label, model, train_data, test_text):
    nlp_train = train(label, train_data, model)
    nlp_test = get_product(test_text,nlp_train)
    return nlp_test

def catch_cat(predict, data):
    for i in data:
        for u in data:
            if u['category'] == predict:
                return u['item_attributes']
            
def store_att(att,my_product):
    my_dict = {'PRODUCT':'','item_attributes':{}}
    for i in my_product:
        if i[-1] == 'PRODUCT':
            my_dict['PRODUCT'] = i[0]
        if i[-1] in att:
            my_dict['item_attributes'][i[-1]] = i[0]
    return my_dict

if __name__ == '__main__':
    # Define the new entity label
    LABEL = "PRODUCT"
    # Define model
    model_name = "en_core_web_sm"
    # Define the training data
    TRAIN_DATA = [
        (
            "This is a great product",
            {
                "entities": [(10, 17, LABEL)]
            },
        ),
        (
            "I love this shampoo",
            {
                "entities": [(12, 19, LABEL)]
            },
        ),
        (
            "The phone has a great camera",
            {
                "entities": [(4, 9, LABEL)]
            },
        ),
    ]
    
    category_list = ["phone", "clothes"]
    
    test_text = "I'm looking for a new , samsung with price 1000$"
    model = train(LABEL,TRAIN_DATA,model_name)
    my_product = get_product(test_text, model)
    predict = get_product_category(my_product, category_list)
    print(f"item: f{my_product}")
    print(f"category: {predict}")
    catch = catch_cat(predict,data)
    stores = store_att(catch,my_product)
    # Write json data 
    with open("cate_list.json", "w") as json_file:  
    # Sử dụng json.dump() để ghi dữ liệu vào file   
        json.dump(stores, json_file) 