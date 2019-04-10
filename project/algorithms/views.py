from flask import render_template, request, redirect, url_for, Blueprint, send_file

## BLUEPRINT INIT
from project.algorithms.models import CodeModel

algorithms_blueprint = Blueprint(
    'algorithms', __name__,
    template_folder="templates"
)

## ALGORITHMS
from .ml_algorithms import *

## SOMMELIER QUOTES
from .messages import rf_message, vot_message, gtb_message


############################################################################# VIEWS #####################################################################################################################################


## MAIN PAGE - "SUMMARY" ###############################################################################################


@algorithms_blueprint.route('/')
def summary():
    dataset_head, describe, rows, columns, counter_sort, counter_dict = dataset_characteristics()

    return render_template("summary.html", describe=describe.to_html(), rows=rows,
                           columns=columns, dataset_head=dataset_head.to_html(),
                           counter_sort=counter_sort.to_html(), counter_dict=counter_dict)


## BUILD CLASSIFIER ####################################################################################################


@algorithms_blueprint.route('/classifier_build', methods=['GET', 'POST'])
def classifier_build():
    X_head, y_head, X_transformed, X_transformed_df, X_train_len, X_test_len, accuracies_initial = build_classifier()

    return render_template("classifier_build.html", X_head=X_head.to_html(),
                           y_head=y_head.to_html(), X_transformed_df=X_transformed_df.to_html(),
                           X_train_len=X_train_len, X_test_len=X_test_len,
                           accuracies_initial=accuracies_initial.to_html())


## FIT CLASSIFIER ######################################################################################################


@algorithms_blueprint.route('/classifier_fit', methods=['GET', 'POST'])
def classifier_fit():
    accuracies_tune = pd.read_csv(accuracies_tune_dataset)
    accuracies_test = pd.read_csv(accuracies_test_dataset)

    return render_template("classifier_fit.html", accuracies_tune=accuracies_tune.to_html(),
                           accuracies_test=accuracies_test.to_html())


@algorithms_blueprint.route('/sommeliers', methods=['GET', 'POST'])
def sommeliers():
    ## Gather User Input with conditioning for blank field
    if request.method == 'POST':

        if request.form['fixed_acidity'] == "":
            fixed_acidity = 8.32
        else:
            fixed_acidity = float(request.form['fixed_acidity'])

        if request.form['volatile_acidity'] == "":
            volatile_acidity = 0.53
        else:
            volatile_acidity = float(request.form['volatile_acidity'])

        if request.form['citric_acid'] == "":
            citric_acid = 0.27
        else:
            citric_acid = float(request.form['citric_acid'])

        if request.form['residual_sugar'] == "":
            residual_sugar = 2.54
        else:
            residual_sugar = float(request.form['residual_sugar'])

        if request.form['chlorides'] == "":
            chlorides = 0.09
        else:
            chlorides = float(request.form['chlorides'])

        if request.form['free_sulfur_dioxide'] == "":
            free_sulfur_dioxide = 15.87
        else:
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])

        if request.form['total_sulfur_dioxide'] == "":
            total_sulfur_dioxide = 46.47
        else:
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])

        if request.form['density'] == "":
            density = 1.00
        else:
            density = float(request.form['density'])

        if request.form['pH'] == "":
            pH = 3.31
        else:
            pH = float(request.form['pH'])

        if request.form['sulphates'] == "":
            sulphates = 0.66
        else:
            sulphates = float(request.form['sulphates'])

        if request.form['alcohol'] == "":
            alcohol = 10.42
        else:
            alcohol = float(request.form['alcohol'])

        red_wine = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                     chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                     density, pH, sulphates, alcohol]]

        ## Predict values

        rf_predict = model_rf.predict(red_wine)
        gtb_predict = model_gtb.predict(red_wine)
        vot_predict = model_vot.predict(red_wine)

        ## Choose sommelier comment

        random_forest_message = rf_message(rf_predict)
        gradient_message = gtb_message(gtb_predict)
        vote_message = vot_message(vot_predict)

        return render_template('sommeliers.html', rf_predict=rf_predict[0],
                               gtb_predict=gtb_predict[0], vot_predict=vot_predict[0],
                               random_forest_message=random_forest_message,
                               gradient_message=gradient_message,
                               vote_message=vote_message)

    return render_template('sommeliers.html')


@algorithms_blueprint.route('/download_code/<code_name>', methods=['GET'])
def download_code(code_name):
    code = os.path.join(my_path, "../../static/datasets/{}.py".format(code_name))

    return send_file(code, as_attachment=True)


## MANAGE DB VIEWS #####################################################################################################


@algorithms_blueprint.route('/manage_db')
def manage_db():
    return render_template('manage_db.html')


@algorithms_blueprint.route('/new_code', methods=['POST'])
def new_code():
    code_file = request.files['inputFile']
    code_file = code_file.read()
    code = CodeModel(name=request.form['name'], file=code_file)
    code.save_to_db()
    return redirect(url_for("algorithms.summary"))
