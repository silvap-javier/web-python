from flask import Flask, render_template,request,jsonify
from pathlib import Path
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tree')
def summary():
    dataset_path_folder = "./"
    dataset_p = Path(dataset_path_folder)
    path_dict = []
    scan_dir(dataset_p, path_dict)
    json_dict = json.dumps(path_dict, sort_keys=True)
    return json_dict

@app.route('/automatic-report-generation')
def automatic_report_generation():
    return render_template('automatic-report-generation.html')

@app.route('/create-img-structure')
def create_img_structure():
    return render_template('create-img-structure.html')

@app.route('/distance-to-root')
def distance_to_root():
    return render_template('distance-to-root.html')

@app.route('/filter-images')
def filter_images():
    return render_template('filter-images.html')

@app.route('/generate-report')
def generate_report ():
    return render_template('generate-report.html')

@app.route('/image-selection')
def image_selection():
    return render_template('image-selection.html')

@app.route('/inspection-data-generator')
def inspection_data_generator():
    return render_template('inspection-data-generator.html')

@app.route('/rename-images')
def rename_images():
    return render_template('rename-images.html')

@app.route('/summary-creation')
def summary_creation ():
    return render_template('summary-creation.html')


@app.route('/run_script', methods=['POST'])
def run_script():
    p = Path.cwd()
    print(p.relative_to)
    actions = {
        'automatic-report-generation' : __automati_report_gen,
        'create-image-structure' : __create_image_structure,
        'nacelle-offset' : __nacelle_offset,
        'filter-images' : __filter_images,
        'image-selection' : __image_selection,
        'rename-images' : __rename_images,
        'summary-creation': __summary_creation
    }
    actionType = request.form['type']
    actions[actionType](request)
    return render_template('result.html')

def __automati_report_gen(request): 
        print('file',request.form['pathFile'])
        print("Private method") 

def __summary_creation(request): 
        print("Private method") 

def __create_image_structure(request): 
        print('output_name',request.form['output_name'])
        print("Private method") 

def __nacelle_offset(request): 
        print('nacelle_offset',request.form['nacelle_offset'])
        print('fit_type',request.form['fit_type'])
        print('show_plot',request.form['show_plot'])
        print("Private method") 

def __image_selection(request): 
        print('nacelle_offset',request.form['nacelle_z_offset'])
        print('fit_type',request.form['min_dist'])
        print("Private method") 

def __filter_images(request): 
        print("Private method") 

def __rename_images(request): 
        print("Private method") 

def scan_dir(dir, path_dict):

    for index, path in enumerate(Path(dir).glob('*')):
        file_dir_dict = {
            'title' : path.name,
            'key' : index,
            'path' : str(path)
        }
        if path.is_file():
            path_dict.append(file_dir_dict)
        else:
            file_dir_dict['folder'] = True
            file_dir_dict['children'] = []
            path_dict.append(file_dir_dict)
            scan_dir(path, file_dir_dict['children'])