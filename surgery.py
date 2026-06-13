import h5py
import os

models_dir = 'models'

for file in os.listdir(models_dir):
    if file.endswith('.h5') and 'fixed' not in file:
        filepath = os.path.join(models_dir, file)
        new_filepath = filepath.replace('.h5', '_fixed.h5')
        
        with h5py.File(filepath, 'r') as f_orig:
            with h5py.File(new_filepath, 'w') as f_new:
                f_orig.copy(f_orig['model_weights'], f_new, 'model_weights')
                
                # FIX: Check if attribute is bytes or str
                config = f_orig.attrs['model_config']
                if isinstance(config, bytes):
                    config = config.decode('utf-8')
                
                new_config = config.replace('conv1/conv', 'conv1_conv')
                f_new.attrs['model_config'] = new_config.encode('utf-8')
                
        print(f"Fixed: {new_filepath}")