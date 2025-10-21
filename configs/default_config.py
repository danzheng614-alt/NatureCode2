import os

# relative file path to trained model
#model_path 指向训练好的 TCN 模型文件 trained_tcn.tar，它存放在项目的 models 文件夹中。
model_path = os.path.join("models", "trained_tcn.tar")

# relative path to data
#data_dir 指向 数据集存放的位置，通常是外部存储的文件夹路径  ".." 表示上一级目录，"data" 是存放数据集的文件夹。
data_dir = "data/Phase1And2_Complete/Complete"
# data_dir = "/home/sxzheng/code/sjyck/Time-Series-Library-main/capsule-5421243-code/data/Phase1And2_Paesed"
# corresponding leg (model is not dependent on side)
#这个变量决定了数据集中的传感器数据将会选取右腿的数据（* 会被替换为 r）。例如，foot_imu_*_gyro_x 会被替换为 foot_imu_r_gyro_x。
side = "r"#定义了 side 变量，表示模型对应的腿部，"r" 表示右腿（"l" 表示左腿）。

# corresponding model input names in dataset (* is substituted with side)
#这行代码定义了一个列表 input_names，列出了所有的输入数据字段名（传感器数据的名称）。其中，* 表示它将被替换为 side（即 "r" 或 "l"，代表左右腿）。
#这些是模型的输入特征数据，包括：IMU 数据、鞋垫数据、关节角度
input_names = ["foot_imu_*_gyro_x", "foot_imu_*_gyro_y", "foot_imu_*_gyro_z", 
				"foot_imu_*_accel_x", "foot_imu_*_accel_y", "foot_imu_*_accel_z", 
				"shank_imu_*_gyro_x", "shank_imu_*_gyro_y", "shank_imu_*_gyro_z", 
				"shank_imu_*_accel_x", "shank_imu_*_accel_y", "shank_imu_*_accel_z", 
				"thigh_imu_*_gyro_x", "thigh_imu_*_gyro_y", "thigh_imu_*_gyro_z", 
				"thigh_imu_*_accel_x", "thigh_imu_*_accel_y", "thigh_imu_*_accel_z",
				"insole_*_cop_x", "insole_*_cop_z", "insole_*_force_y",
				"hip_angle_*", "hip_angle_*_velocity_filt", 
				"knee_angle_*", "knee_angle_*_velocity_filt"]

# corresponding model label names in dataset
#这行代码定义了一个列表 label_names，列出了所有的标签数据字段名。标签数据通常表示模型的目标值。
label_names = ["hip_flexion_*_moment", "knee_angle_*_moment"]

# intentional model delay (in data points)
#model_delays 列表表示模型的延迟，单位是数据点。这里表示：hip moment（髋关节力矩）的估算值延迟了 10 个数据点knee angle moment（膝关节力矩）的估算值没有延迟，即 0。
model_delays = [10, 0] # hip moment estimates are delayed by 50 ms

# participant masses for normalizing insole forces.参与者的体重数据,这个数据在模型中用于归一化鞋垫压力数据
#体重归一化：鞋垫上的压力数据会根据参与者的体重进行归一化，以消除体重差异对数据的影响。
# - NOTE: This is a simplification. Detailed participant masses are provided in the readme of the corresponding dataset.
participant_masses = {
	"BT01": 80.59,
	"BT02": 72.24,
	"BT03": 95.29,
	"BT04": 98.23,
	"BT06": 79.33,
	"BT07": 64.49,
	"BT08": 69.13,
	"BT09": 82.31,
	"BT10": 93.45,
	"BT11": 50.39,
	"BT12": 78.15,
	"BT13": 89.85,
	"BT14": 67.30,
	"BT15": 58.40,
	"BT16": 64.33,
	"BT17": 60.03,
	"BT18": 67.96,
	"BT19": 69.95,
	"BT20": 55.44,
	"BT21": 58.85,
	"BT22": 76.79,
	"BT23": 67.23,
	"BT24": 77.79
}

