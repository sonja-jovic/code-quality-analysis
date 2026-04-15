import tensorflow as tf

def build_tf_model():

    model = tf.keras.Sequential([

        tf.keras.layers.Dense(16, activation="relu", input_shape=(4,)),

        tf.keras.layers.Dense(8, activation="relu"),

        tf.keras.layers.Dense(3, activation="softmax")

    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model