def plot_grid(nrows, ncols, data,labels):
  fig, a = plt.subplots(nrows,ncols, figsize = [10,10])
  fig.tight_layout()
  data = data.permute(0,2,3,1)
  for i in range(nrows):
    for j in range(ncols):
      img = data[i+j][:,:,0]
      a[i][j].imshow(img, cmap = 'gray')
      a[i][j].set_title(class_map[int(labels[i+j])])
      a[i][j].set_xticks([])
      a[i][j].set_yticks([])
