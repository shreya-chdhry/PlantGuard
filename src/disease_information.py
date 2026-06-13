model_mapping_dict = {
    'Apple': {
        'classes': ['Apple Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy'],
        'model_path': 'apple_model_fixed.h5'
    },
    'Cherry': {
        'classes': ['Healthy', 'Powdery Mildew'],
        'model_path': 'cherry_model_fixed.h5'
    },
    'Corn': {
        'classes': ['Common Rust', 'Gray Leaf Spot', 'Healthy', 'Northern Leaf Blight'],
        'model_path': 'corn_model_fixed.h5'
    },
    'Grape': {
        'classes': ['Black Rot', 'Esca', 'Healthy', 'Leaf Blight'],
        'model_path': 'grape_model_fixed.h5'
    },
    'Peach': {
        'classes': ['Bacterial Spot', 'Healthy'],
        'model_path': 'peach_model_fixed.h5'
    },
    'Pepper': {
        'classes': ['Bacterial Spot', 'Healthy'],
        'model_path': 'pepper_model_fixed.h5'
    },
    'Potato': {
        'classes': ['Early Blight', 'Healthy', 'Late Blight'],
        'model_path': 'potato_model_fixed.h5'
    },
    'Strawberry': {
        'classes': ['Healthy', 'Leaf Scorch'],
        'model_path': 'strawberry_model_fixed.h5'
    },
    'Tomato': {
        'classes': ['Bacterial Spot', 'Early Blight', 'Healthy', 'Late Blight', 'Leaf Mold', 'Septoria Leaf Spot', 'Spider Mites', 'Target Spot', 'Mosaic Virus', 'Yellow Leaf Curl Virus'],
        'model_path': 'tomato_model_fixed.h5'
    }
}

plant_disease_dict = {
    'Healthy': {
        'Description': '*A healthy plant exhibits vigorous growth and has no visible signs of disease or pest infestation. The leaves are typically green and free from discoloration, spots, or lesions. The stems are firm and erect, and the overall plant appearance is robust.*',
        'Symptoms': '*No symptoms; plant appears normal and free from any abnormalities.*',
        'Treatment': '*No treatment is required for a healthy plant. However, proper cultural practices such as adequate watering, fertilization, and pest management can help maintain plant health.*'
    },
    'Apple': {
        'Apple Scab': {
            'Description': '*Apple scab is a fungal disease that causes dark, scabby marks on the leaves and fruit of apple and crabapple trees.*',
            'Symptoms': '*Small, brown or olive-green spots on the underside of young leaves, or on either side of older leaves.*',
            'Treatment': '*Practice good sanitation by removing fallen leaves and fruit from the ground. Apply fungicides as directed.*'
        },
        'Black Rot': {
            'Description': '*Black rot is a disease caused by the fungus Botryosphaeria obtusa that affects apple trees.*',
            'Symptoms': '*Small purple spots that develop into brownish-tan centers with darker margins, giving a "frog-eye" appearance.*',
            'Treatment': '*Prune infected branches and remove and destroy infected fruit. Apply fungicides during the growing season.*'
        },
        'Cedar Apple Rust': {
            'Description': '*Cedar apple rust is a fungal disease that affects apple and cedar trees, appearing as orange or yellow spots.*',
            'Symptoms': '*Orange or yellow spots on the leaves and fruit. Spore-producing structures may form on the underside of leaves.*',
            'Treatment': '*Remove and destroy infected plant material. Prune nearby cedar trees to reduce spore production.*'
        }
    },
    'Cherry': {
        'Powdery Mildew': {
            'Description': '*Powdery mildew appears as white, powdery spots on the leaves and shoots of cherry trees.*',
            'Symptoms': '*White, powdery spots on leaves and shoots. Infected leaves may become distorted or yellowed.*',
            'Treatment': '*Remove and destroy infected plant material. Improve air circulation and apply fungicides labeled for powdery mildew.*'
        }
    },
    'Corn': {
        'Common Rust': {
            'Description': '*Common rust is a fungal disease appearing as small, reddish-brown pustules on corn leaves.*',
            'Symptoms': '*Small, reddish-brown pustules on the upper surfaces of corn leaves.*',
            'Treatment': '*Plant resistant corn varieties. Practice good crop rotation. Apply fungicides if necessary.*'
        },
        'Gray Leaf Spot': {
            'Description': '*Gray leaf spot appears as small, rectangular lesions with tan centers on corn leaves.*',
            'Symptoms': '*Small, rectangular lesions with tan centers and dark brown to purple margins on the leaves.*',
            'Treatment': '*Plant resistant corn varieties. Practice good crop rotation and apply fungicides preventatively.*'
        },
        'Northern Leaf Blight': {
            'Description': '*Northern leaf blight appears as large, cigar-shaped lesions on corn leaves.*',
            'Symptoms': '*Large, cigar-shaped lesions with tan centers and dark brown to gray margins on the leaves.*',
            'Treatment': '*Plant resistant corn varieties, rotate crops, and apply fungicides preventatively.*'
        }
    },
    'Grape': {
        'Black Rot': {
            'Description': '*Black rot is a fungal disease appearing as black, necrotic lesions on grapevine leaves and fruit.*',
            'Symptoms': '*Black, necrotic lesions on the leaves, shoots, and fruit. Infected fruit may shrivel and become mummified.*',
            'Treatment': '*Remove and destroy infected material. Practice proper pruning and air circulation. Apply fungicides.*'
        },
        'Esca': {
            'Description': '*Esca is a complex of fungal diseases causing leaf discoloration and wood necrosis in grapevines.*',
            'Symptoms': '*Yellow or reddish-brown discoloration of leaves ("tiger-striped"), internal wood necrosis, and shoot dieback.*',
            'Treatment': '*Pruning and canopy management can help. Application of fungicides may provide limited control.*'
        },
        'Leaf Blight': {
            'Description': '*Leaf blight appears as brown, necrotic lesions on grapevine leaves.*',
            'Symptoms': '*Brown, necrotic lesions on the leaves, often with a yellow halo around the edges.*',
            'Treatment': '*Remove and destroy infected material. Improve air circulation. Apply fungicides preventatively.*'
        }
    },
    'Peach': {
        'Bacterial Spot': {
            'Description': '*Bacterial spot affects peach leaves, fruit, and shoots, appearing as small lesions.*',
            'Symptoms': '*Small, water-soaked lesions on leaves, which turn brown with yellow halos.*',
            'Treatment': '*Remove and destroy infected material. Apply copper-based fungicides. Prune to improve air circulation.*'
        }
    },
    'Pepper': {
        'Bacterial Spot': {
            'Description': '*Bacterial spot affects pepper leaves, fruit, and stems, favored by warm, humid weather.*',
            'Symptoms': '*Small, water-soaked lesions on leaves, turning brown with yellow halos.*',
            'Treatment': '*Sanitation is key. Apply copper-based bactericides and prune to improve air circulation.*'
        }
    },
    'Potato': {
        'Early Blight': {
            'Description': '*Early blight appears as dark, concentric rings on potato leaves.*',
            'Symptoms': '*Dark, concentric rings with yellow halos on leaves, starting from the lower leaves.*',
            'Treatment': '*Sanitation, proper crop rotation, and fungicides as directed.*'
        },
        'Late Blight': {
            'Description': '*Late blight is a devastating disease affecting potato leaves, stems, and tubers.*',
            'Symptoms': '*Dark, water-soaked lesions on leaves and stems, often with white, fuzzy growth on undersides.*',
            'Treatment': '*Remove infected material. Fungicides are necessary. Rotate crops and avoid overhead irrigation.*'
        }
    },
    'Strawberry': {
        'Leaf Scorch': {
            'Description': '*Leaf scorch appears as brown, necrotic spots on strawberry leaves.*',
            'Symptoms': '*Brown, necrotic spots on leaves, which may enlarge and coalesce.*',
            'Treatment': '*Remove and destroy infected material. Avoid overhead irrigation and apply fungicides.*'
        }
    },
    'Tomato': {
        'Bacterial Spot': {
            'Description': '*Bacterial spot affects tomato leaves and fruit, causing significant damage in humid conditions.*',
            'Symptoms': '*Small, water-soaked lesions on leaves, turning brown with yellow halos.*',
            'Treatment': '*Sanitation, copper-based fungicides, and pruning.*'
        },
        'Early Blight': {
            'Description': '*Early blight appears as dark, concentric rings on tomato leaves and fruit.*',
            'Symptoms': '*Dark, concentric rings with yellow halos on leaves.*',
            'Treatment': '*Sanitation, crop rotation, and fungicides.*'
        },
        'Late Blight': {
            'Description': '*Late blight is a devastating fungal disease affecting tomato leaves, stems, and fruit.*',
            'Symptoms': '*Dark, water-soaked lesions on leaves, stems, and fruit, often with white, fuzzy growth.*',
            'Treatment': '*Sanitation, fungicides, and avoiding overhead irrigation.*'
        }
    }
}