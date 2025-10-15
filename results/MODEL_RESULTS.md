###############################################################################
###############################################################################


XGBOOST RESULTS: 

== Params ==
'clf__colsample_bytree': np.float64(0.5740434649766999), 
'clf__gamma': np.float64(4.98870242524471), 
'clf__learning_rate': np.float64(0.09003430428258549), 
'clf__max_depth': 4, 
'clf__n_estimators': 229, 
'clf__random_state': 42, 
'clf__reg_alpha': np.float64(0.4110370133182313), 
'clf__reg_lambda': np.float64(0.033050732900548385), 
'clf__subsample': np.float64(0.6725356240133415)

== TEST Accuracy Report ==

Accuracy: 0.3259

              precision    recall  f1-score   support

           0     0.3038    0.5000    0.3780        48
           1     0.1667    0.0323    0.0541        31
           2     0.0000    0.0000    0.0000        15
           3     0.1951    0.2623    0.2238        61
           4     0.0000    0.0000    0.0000        15
           5     0.3285    0.3846    0.3543       117
           6     0.4286    0.2727    0.3333        11
           7     0.3333    0.2391    0.2785        46
           8     0.0000    0.0000    0.0000        17
           9     0.4178    0.4586    0.4373       133

    accuracy                         0.3259       494
   macro avg     0.2174    0.2150    0.2059       494
weighted avg     0.2949    0.3259    0.3028       494


Test Set AUC (OvR): 0.7244

== Confidence Decile Table ==

      Top %  N Samples  Correct Predictions  Accuracy in Decile  Avg Confidence
0   Top 10%         49                   34               0.694           0.531  
1   Top 20%         98                   55               0.561           0.482
2   Top 30%        148                   71               0.480           0.443  
3   Top 40%        197                   89               0.452           0.413  
4   Top 50%        247                  105               0.425           0.389  
5   Top 60%        296                  115               0.389           0.369  
6   Top 70%        345                  128               0.371           0.353  
7   Top 80%        395                  142               0.359           0.338
8   Top 90%        444                  152               0.342           0.324  
9  Top 100%        494                  161               0.326           0.309  


###############################################################################
###############################################################################


SVC RESULTS

== Params ==
'clf__C': np.float64(3.9246199126716275), 
'clf__degree': 2, 
'clf__gamma': 'scale', 
'clf__kernel': 'rbf', 
'clf__random_state': 42

== TEST Accuracy Report ==

Accuracy: 0.2874
              precision    recall  f1-score   support

           0     0.2281    0.5417    0.3210        48
           1     0.0000    0.0000    0.0000        31
           2     0.0000    0.0000    0.0000        15
           3     0.1429    0.0164    0.0294        61
           4     0.0000    0.0000    0.0000        15
           5     0.2936    0.5897    0.3920       117
           6     0.2000    0.1818    0.1905        11
           7     0.2222    0.1739    0.1951        46
           8     0.0000    0.0000    0.0000        17
           9     0.4091    0.2707    0.3258       133

    accuracy                         0.2874       494
   macro avg     0.1496    0.1774    0.1454       494
weighted avg     0.2446    0.2874    0.2378       494


Test Set AUC (OvR): 0.6920

== Confidence Decile Table ==

      Top %  N Samples  Correct Predictions  Accuracy in Decile   Avg Confidence
0   Top 10%         49                   25               0.510            0.371
1   Top 20%         98                   39               0.398            0.351
2   Top 30%        148                   55               0.372            0.336 
3   Top 40%        197                   65               0.330            0.324  
4   Top 50%        247                   83               0.336            0.314
5   Top 60%        296                   97               0.328            0.305
6   Top 70%        345                  105               0.304            0.296 
7   Top 80%        395                  121               0.306            0.288
8   Top 90%        444                  131               0.295            0.279  
9  Top 100%        494                  141               0.285            0.270  


################################################################################
################################################################################


RANDOM FORREST RESULTS:

== Params ==
'clf__bootstrap': True, 
'clf__class_weight': None, 
'clf__max_depth': 20, 
'clf__max_features': 'log2', 
'clf__min_samples_leaf': 4, 
'clf__min_samples_split': 3, 
'clf__n_estimators': 269, 
'clf__random_state': 42

== TEST Accuracy Report ==

Accuracy: 0.3138
              precision    recall  f1-score   support

           0     0.3125    0.6250    0.4167        48
           1     0.0000    0.0000    0.0000        31
           2     0.0000    0.0000    0.0000        15
           3     0.1061    0.1148    0.1102        61
           4     0.0000    0.0000    0.0000        15
           5     0.3259    0.3761    0.3492       117
           6     0.2000    0.1818    0.1905        11
           7     0.3333    0.2609    0.2927        46
           8     0.0000    0.0000    0.0000        17
           9     0.4138    0.4511    0.4317       133

    accuracy                         0.3138       494
   macro avg     0.1692    0.2010    0.1791       494
weighted avg     0.2676    0.3138    0.2845       494


Test Set AUC (OvR): 0.7373

== Confidence Decile Table ==

      Top %  N Samples  Correct Predictions  Accuracy in Decile   Avg Confidence
0   Top 10%         49                   32               0.653            0.472 
1   Top 20%         98                   53               0.541            0.430 
2   Top 30%        148                   71               0.480            0.401
3   Top 40%        197                   88               0.447            0.377
4   Top 50%        247                   97               0.393            0.358
5   Top 60%        296                  112               0.378            0.341 
6   Top 70%        345                  126               0.365            0.326 
7   Top 80%        395                  136               0.344            0.312 
8   Top 90%        444                  145               0.327            0.300 
9  Top 100%        494                  155               0.314            0.287 


################################################################################
################################################################################


MULTI-LAYER PERCEPTRON RESULTS: 

== Params ==
'clf__activation': 'logistic', 
'clf__alpha': np.float64(4.1306144511331714e-05), 
'clf__early_stopping': True, 
'clf__hidden_layer_sizes': (256, 128, 64), 
'clf__learning_rate': 'adaptive', 
'clf__learning_rate_init': np.float64(0.006487477066058677), 
'clf__random_state': 42, 
'clf__solver': 'adam'

== TEST Accuracy Report ==

Accuracy: 0.3279
              precision    recall  f1-score   support

           0     0.2840    0.4792    0.3566        48
           1     0.0000    0.0000    0.0000        31
           2     0.0000    0.0000    0.0000        15
           3     0.2037    0.3607    0.2604        61
           4     0.0000    0.0000    0.0000        15
           5     0.3091    0.2906    0.2996       117
           6     0.3750    0.2727    0.3158        11
           7     0.3478    0.3478    0.3478        46
           8     0.0000    0.0000    0.0000        17
           9     0.4571    0.4812    0.4689       133

    accuracy                         0.3279       494
   macro avg     0.1977    0.2232    0.2049       494
weighted avg     0.2898    0.3279    0.3034       494


Test Set AUC (OvR): 0.7054

== Confidence Decile Table ==

      Top %  N Samples  Correct Predictions  Accuracy in Decile   Avg Confidence
0   Top 10%         49                   29               0.592            0.574
1   Top 20%         98                   53               0.541            0.529
2   Top 30%        148                   70               0.473            0.498 
3   Top 40%        197                   87               0.442            0.474 
4   Top 50%        247                  102               0.413            0.450 
5   Top 60%        296                  119               0.402            0.426
6   Top 70%        345                  129               0.374            0.403 
7   Top 80%        395                  141               0.357            0.383 
8   Top 90%        444                  149               0.336            0.365  
9  Top 100%        494                  162               0.328            0.347


################################################################################
################################################################################


LOGISTIC REGRESSION RESULTS:

== Params ==

'clf__C': np.float64(0.0013342990285187936), 
'clf__l1_ratio': None, 
'clf__penalty': 'l2', 
'clf__random_state': 42, 
'clf__solver': 'newton-cg'

== TEST Accuracy Report ==

Accuracy: 0.3320
              precision    recall  f1-score   support

           0     0.2500    0.5625    0.3462        48
           1     0.0000    0.0000    0.0000        31
           2     0.0000    0.0000    0.0000        15
           3     0.1667    0.0164    0.0299        61
           4     0.0000    0.0000    0.0000        15
           5     0.3333    0.5812    0.4237       117
           6     0.3333    0.0909    0.1429        11
           7     0.4091    0.1957    0.2647        46
           8     0.0000    0.0000    0.0000        17
           9     0.3946    0.4361    0.4143       133

    accuracy                         0.3320       494
   macro avg     0.1887    0.1883    0.1622       494
weighted avg     0.2756    0.3320    0.2770       494


Test Set AUC (OvR): 0.6775

== Confidence Decile Table ==

      Top %  N Samples  Correct Predictions  Accuracy in Decile   Avg Confidence
0   Top 10%         49                   33               0.673            0.364
1   Top 20%         98                   50               0.510            0.322
2   Top 30%        148                   68               0.459            0.300 
3   Top 40%        197                   86               0.437            0.285
4   Top 50%        247                   97               0.393            0.273
5   Top 60%        296                  109               0.368            0.264 
6   Top 70%        345                  120               0.348            0.255 
7   Top 80%        395                  134               0.339            0.247 
8   Top 90%        444                  150               0.338            0.240  
9  Top 100%        494                  164               0.332            0.232  


################################################################################
################################################################################


LINEAR DISCRIMINANT ANALYSYS:

== Params ==
'clf__shrinkage': 0.7, 
'clf__solver': 'lsqr'

== TEST Accuracy Report ==

Accuracy: 0.3077
              precision    recall  f1-score   support

           0     0.3636    0.4167    0.3883        48
           1     0.1316    0.1613    0.1449        31
           2     0.0000    0.0000    0.0000        15
           3     0.2000    0.2787    0.2329        61
           4     0.2000    0.1333    0.1600        15
           5     0.3125    0.2991    0.3057       117
           6     0.2143    0.2727    0.2400        11
           7     0.2500    0.3043    0.2745        46
           8     0.0000    0.0000    0.0000        17
           9     0.4590    0.4211    0.4392       133

    accuracy                         0.3077       494
   macro avg     0.2131    0.2287    0.2186       494
weighted avg     0.3000    0.3077    0.3020       494


Test Set AUC (OvR): 0.7132

== Confidence Decile Table ==

      Top %  N Samples  Correct Predictions  Accuracy in Decile   Avg Confidence
0   Top 10%         49                   21               0.429            0.744
1   Top 20%         98                   43               0.439            0.651
2   Top 30%        148                   64               0.432            0.598 
3   Top 40%        197                   80               0.406            0.560 
4   Top 50%        247                   93               0.377            0.530
5   Top 60%        296                  109               0.368            0.505 
6   Top 70%        345                  121               0.351            0.485
7   Top 80%        395                  130               0.329            0.465 
8   Top 90%        444                  140               0.315            0.447  
9  Top 100%        494                  152               0.308            0.425


################################################################################
################################################################################


K-NEAREST NEIGHBORS RESULTS: 

== Params ==
'clf__n_neighbors': 19, 
'clf__p': 1, 
'clf__weights': 'uniform'

== TEST Accuracy Report ==

Accuracy: 0.2571
              precision    recall  f1-score   support

           0     0.3038    0.5000    0.3780        48
           1     0.0000    0.0000    0.0000        31
           2     0.0000    0.0000    0.0000        15
           3     0.1150    0.2131    0.1494        61
           4     0.2000    0.0667    0.1000        15
           5     0.2956    0.4017    0.3406       117
           6     0.1818    0.1818    0.1818        11
           7     0.2857    0.2609    0.2727        46
           8     1.0000    0.0588    0.1111        17
           9     0.4655    0.2030    0.2827       133

    accuracy                         0.2571       494
   macro avg     0.2847    0.1886    0.1816       494
weighted avg     0.3102    0.2571    0.2483       494


Test Set AUC (OvR): 0.6523

== Confidence Decile Table ==

      Top %  N Samples  Correct Predictions  Accuracy in Decile   Avg Confidence
0   Top 10%         49                   18               0.367            0.515 
1   Top 20%         98                   38               0.388            0.470  
2   Top 30%        148                   55               0.372            0.439 
3   Top 40%        197                   68               0.345            0.420 
4   Top 50%        247                   77               0.312            0.399 
5   Top 60%        296                   87               0.294            0.385  
6   Top 70%        345                   98               0.284            0.368  
7   Top 80%        395                  108               0.273            0.355 
8   Top 90%        444                  120               0.270            0.340  
9  Top 100%        494                  127               0.257            0.326 


################################################################################
################################################################################


EXTRA TREE RESULTS: 

== Params ==

'clf__bootstrap': True, 
'clf__max_depth': 5, 
'clf__max_features': None, 
'clf__min_samples_leaf': 9, 
'clf__min_samples_split': 5, 
'clf__n_estimators': 372, 
'clf__random_state': 42

== TEST Accuracy Report ==

Accuracy: 0.3826
              precision    recall  f1-score   support

           0     0.4559    0.6458    0.5345        48
           1     0.3158    0.1935    0.2400        31
           2     0.0000    0.0000    0.0000        15
           3     0.1429    0.0492    0.0732        61
           4     0.0000    0.0000    0.0000        15
           5     0.3412    0.4957    0.4042       117
           6     0.4000    0.1818    0.2500        11
           7     0.4400    0.2391    0.3099        46
           8     0.0000    0.0000    0.0000        17
           9     0.4194    0.5865    0.4890       133

    accuracy                         0.3826       494
   macro avg     0.2515    0.2392    0.2301       494
weighted avg     0.3253    0.3826    0.3378       494


Test Set AUC (OvR): 0.7765

== Confidence Decile Table ==

      Top %  N Samples  Correct Predictions  Accuracy in Decile   Avg Confidence
0   Top 10%         49                   34               0.694            0.458
1   Top 20%         98                   54               0.551            0.414
2   Top 30%        148                   76               0.514            0.384  
3   Top 40%        197                  100               0.508            0.360 
4   Top 50%        247                  118               0.478            0.340 
5   Top 60%        296                  133               0.449            0.324
6   Top 70%        345                  148               0.429            0.310 
7   Top 80%        395                  169               0.428            0.297 
8   Top 90%        444                  183               0.412            0.286
9  Top 100%        494                  189               0.383            0.274


################################################################################
################################################################################


FINAL ENSEMLE RESULTS: 

== Parameters ==
'clf__et__max_depth': 20, 
'clf__et__min_samples_leaf': 1, 
'clf__et__n_estimators': 958, 
'clf__log_reg__C': np.float64(0.0006588639614528129), 
'clf__mlp__activation': 'relu', 
'clf__mlp__alpha': np.float64(3.85653172695586e-05), 
'clf__mlp__hidden_layer_sizes': (128,), 
'clf__mlp__learning_rate_init': np.float64(0.005235766264503467), 
'clf__rf__max_depth': None, 
'clf__rf__min_samples_leaf': 1, 
'clf__rf__n_estimators': 975, 
'clf__xgb__colsample_bytree': np.float64(0.7634675496716142), 
'clf__xgb__gamma': np.float64(2.18756236918524), 
'clf__xgb__learning_rate': np.float64(0.0005723198798683331), 
'clf__xgb__max_depth': 14, 
'clf__xgb__n_estimators': 1232, 
'clf__xgb__subsample': np.float64(0.46315551111820746)

== Weights ==
Best Weights: (3, 1, 3, 2, 3, 3)
Combined AUC/Precision Score: 0.5123

== TEST Evaluation ==
Accuracy:  0.3158
AUC (OvR): 0.6863
Precision: 0.3383

Classification Report:

              precision    recall  f1-score     support
0              0.318841  0.458333  0.376068   48.000000
1              0.115385  0.096774  0.105263   31.000000
2              0.333333  0.066667  0.111111   15.000000
3              0.265060  0.360656  0.305556   61.000000
4              0.230769  0.200000  0.214286   15.000000
5              0.352941  0.410256  0.379447  117.000000
6              0.083333  0.181818  0.114286   11.000000
7              0.166667  0.173913  0.170213   46.000000
8              0.200000  0.058824  0.090909   17.000000
9              0.528736  0.345865  0.418182  133.000000

accuracy       0.315789  0.315789  0.315789    0.315789
macro avg      0.259506  0.235311  0.228532  494.000000
weighted avg   0.338281  0.315789  0.314737  494.000000


== Weighted Ensemble — Confidence Decile Table ==

       Top %  Accuracy  Avg Confidence
0     Top 5%     0.625           0.461
1    Top 10%     0.551           0.419
2    Top 15%     0.473           0.395
3    Top 20%     0.439           0.379
4    Top 25%     0.415           0.366
5    Top 30%     0.385           0.355
6    Top 35%     0.360           0.346
7    Top 40%     0.345           0.337
8    Top 45%     0.351           0.329
9    Top 50%     0.348           0.322
10   Top 55%     0.351           0.316
11   Top 60%     0.351           0.310
12   Top 65%     0.349           0.305
13   Top 70%     0.354           0.299
14   Top 75%     0.343           0.294
15   Top 80%     0.339           0.289
16   Top 85%     0.334           0.284
17   Top 90%     0.322           0.279
18   Top 95%     0.318           0.274
19  Top 100%     0.316           0.268


################################################################################
################################################################################