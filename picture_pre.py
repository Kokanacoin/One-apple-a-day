from PIL import Image
import glob
from tqdm import tqdm





'''
	批量修改图片格式

	现在只支持对 png、 jpg、 jpeg 的转换
	
	@author kokana
	@param input_file 输入文件夹
	@param output_file 输出文件夹
	@param change_name_flag 是否更改文件名
							默认不更改
							用于混乱的爬去文件名，会按照读取顺序的数字变更名字。
	@param target_Extension 目标扩展名
							默认转换成png
'''
def changeExtensionBatch(input_file, output_file,change_name_flag = False,target_Extension = 'png'):

	def change(path_in, path_out):

		t_e = target_Extension

		if t_e.upper() == 'JPG':
			t_e = 'JPEG'

		img = Image.open(path_in)
		img = img.convert("RGB")
		img.save(path_out, t_e.upper(), quality=80, optimize=True, progressive=True)

	input_list = glob.glob(input_file+'/*')

	for index,every_file in enumerate(tqdm(input_list)):
		
		name = every_file.split('/')[-1]
		e_n = name.split('.')[-1]
		f_n = name[:-(len(e_n) + 1)]

		if change_name_flag:
			change(every_file, output_file + '/' +str(index) + '.' + target_Extension)
		else:
			change(every_file, output_file + '/' +f_n + '.' + target_Extension)

'''
	批量修改图片大小

	
	@author kokana
	@param input_file 输入文件夹
	@param output_file 输出文件夹
	@param width 目标宽度
	@param height 目标高度
'''
def changeSizeBatch(input_file, output_file, width, height):

	input_list = glob.glob(input_file+'/*')

	for index,every_file in enumerate(tqdm(input_list)):

		file_name = every_file.split('/')[-1]
		img = Image.open(every_file)
		img = img.resize((width, height))
		img.save(output_file+'/'+file_name, quality=80, optimize=True, progressive=True)


		



if __name__ == '__main__':
	
	#例子：

	#changeExtension('./picture','./new_picture',change_name_flag=True,target_Extension='png')
	# changeSizeBatch('./new_picture','./resize_picture',128,128)

	pass


























