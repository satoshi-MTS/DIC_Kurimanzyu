# モジュールのインプット
import matplotlib.pyplot as plt


# 関数の宣言
def baibain(start_volume, goal_volume):
	"""
	function : ある物体の体積[start_volume]がバイバインを使用した際、
			   目標の体積[goal_volume]を何時間[number_of_hours]何分[number_of_minutes]で超えるか計算する関数

	:param start_volume: float
		バイバインを使用する物体の体積
	:param goal_volume: float
		目標の体積
	volume : int (計算用)
		バイバインを使用している最中の物体の体積
	number_of_5minutes : int (計算用)
		5分で倍になるバイバインの計算用の値
	list_of_minutes : list (グラフ用)
		グラフのx軸　分数
	list_of_volume : list (グラフ用)
		グラフのy軸　体積
	:return number_of_hours : int
		目標の体積を超えるのに必要な時間
	:return number_of_minutes : int
		目標の体積を超えるのに必要な分数
	"""

	# パラメータの設定
	list_of_minutes = []
	list_of_volume = []
	volume = start_volume
	number_of_5minutes = 0

	# 計算
	while volume < goal_volume:
		volume = start_volume * (2 ** number_of_5minutes)
		list_of_volume.append(volume)
		number_of_5minutes += 1
		list_of_minutes.append(number_of_5minutes * 5)

	# 時間及び分数への換算
	number_of_hours = number_of_5minutes // 12
	number_of_minutes = number_of_5minutes % 12 * 5

	# グラフのプロット
	plt.title('baibain graph')
	plt.xlabel('minutes')
	plt.ylabel('volume')
	plt.plot(list_of_minutes, list_of_volume)
	plt.show()

	# 返り値の設定
	return number_of_hours, number_of_minutes


# パラメータの設定
VOLUME_OF_KURIMANZYU = 10e-4
VOLUME_OF_THE_UNIVERSE = 3e+80

# 結果の表示
print('体積{}[m^3]の栗まんじゅうにバイバインを使用した際、体積{:e}[m^3]の太陽系の大きさを超えるためには{}時間{}分必要です。'
	     .format(VOLUME_OF_KURIMANZYU, VOLUME_OF_THE_UNIVERSE, baibain(VOLUME_OF_KURIMANZYU, VOLUME_OF_THE_UNIVERSE)[0],
				  baibain(VOLUME_OF_KURIMANZYU, VOLUME_OF_THE_UNIVERSE)[1]))
