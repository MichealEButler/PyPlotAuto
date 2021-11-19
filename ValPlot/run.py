import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import csv
from pathlib import Path

#PLOT LABELS
elm = "Elm"
pine = "Pine"
oak = "Oak"
alder = "Alder"
hazel = "Hazel"
ash = "Ash"
lime = "Lime"
birch = "Birch"
horn = "Hornbeam"
larch = "Larch"
beech = "Beech"
willow = "Willow"
maple = "Maple"
pft = "PFT"
elmR = "Elm-R"
pineR = "Pine-R"
oakR = "Oak-R"
alderR = "Alder-R"
hazelR = "Hazel-R"
ashR = "Ash-R"
limeR = "Lime-R"
birchR = "Birch-R"
hornR = "Hornbeam-R"
larchR = "Larch-R"
beechR = "Beech-R"
willowR = "Willow-R"
mapleR = "Maple-R"
pftR = "PFT-R"

#DIRECTORIES
working_folder = Path("D:/Uni Work/Elm Decline Model/Bunce Results/")
date_folder = "16-04-20/"
site_folder = "Hoads/"

inDir = Path("D:/Uni Work/Elm Decline Model/Bunce Results/01-06-20/station/Scarry/Averaged/")
outDir = Path("D:/Uni Work/Elm Decline Model/Bunce Results/01-06-20/station/Scarry/Averaged/Plots/")

gRow = 0

class StoreData():
  def __init__(self, filename):
    with open(filename, "r") as f_input:
      csv_input = csv.reader(f_input)
      self.details = list(csv_input)

  def get_col_row(self, col, row):
    return self.details[row - 1][col - 1]

def check_sim_row(data):
  n = 0.0
  y = []

  for i in range(14): # reads through the second row of the data
    out = data.get_col_row(i+1, 2)
    n = int(out)
    if n > 0:
      y.append(i)
    #print(n)

  return(y)
  #print(y)

def check_bunce_row(data):
  n = 0.0

  start = []
  end = []

  for i in range(14):  # reads through first row of the data
    out = data.get_col_row(i + 15, 2)
    n = int(out)
    if n > 0:
      start.append(i+14)

  for i in range(14):  # reads through last row of the data
    out = data.get_col_row(i + 15, 32)
    n = int(out)
    if n > 0:
       end.append(i+14)

  #return (y)
  #print(start)
  #print(end)
  return(start)

def plot_data(filename, nRow):

  it = 0 #iterator for year
  x = []
  y = []
  species = int(nRow)+1
  value = int(nRow)

  with open(filename, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)
    for row in plots:
      num = row[nRow]
      x.append(it)
      y.append(float(num))
      it += 1

  plt.subplot(2, 2, 1)
  plt.plot(x, y, marker=' ',c=set_line_color(species))
  plt.title('Simulation')
  plt.xlabel('time (y)')
  plt.ylabel('n',rotation=0)


def plot_bunce_data(data, nRow):

  it = 0 #iterator for year
  species = int(nRow)-13
  value = int(nRow)
  x = [0,30]
  start = int(data.get_col_row(value + 1, 2))
  end = int(data.get_col_row(value + 1, 32))
  y = [start, end]

  plt.subplot(2, 2, 2)
  plt.plot(x, y, '--', marker='o', c=set_line_color(species))
  #plt.annotate(start, (0,start), textcoords="offset points", xytext=(0,10), ha='center')
  #plt.annotate(start, (30, end), textcoords="offset points", xytext=(0, 10), ha='center')
  plt.title('Bunce')
  plt.xlabel('time (y)')
  plt.ylabel('n',rotation=0)

def bunce_data(data):
  it = 0  # iterator for year
  ref = check_bunce_row(data)
  length = len(ref)

  for i in range(length):
    n = int(ref[i])
    plot_bunce_data(data, n)

def gen_plot_iterate(data, filename):
  ref = check_sim_row(data)
  length = len(ref)

  for i in range(length):
    n = int(ref[i])
    plot_data(filename, n)
    #plt.show()

def set_line_color(species):
    #set color depending on species
    if species == 1:
       return 'tab:red' #

    if species == 2:
       return 'tab:green' #

    if species == 3:
       return 'tab:blue' #

    if species == 4:
       return 'tab:orange' #

    if species == 5:
       return 'tab:cyan' #

    if species == 6:
       return 'tab:olive' #

    if species == 7:
       return 'tab:purple' #

    if species == 8:
       return 'tab:pink' #

    if species == 9:
       return 'tab:grey' #

    if species == 10:
       return 'tab:gray' #

    if species == 11:
       return 'tab:brown' #

    if species == 12:
       return 'darkolivegreen' #

    if species == 13:
       return 'navy' #

    if species == 14:
       return 'peru' #


def main():
  title = "Plot "
  part1 = "plot"
  part2 = ".txt"
  part3 = ".png"

  for i in range(16):
    file = part1 + str(i+1) + part2
    image = part1 + str(i+1) + part3
    data = StoreData(inDir / file)
    plt.figure()
    plt.suptitle(title + str(i+1),x=0.1,fontsize=14)
    bunce_data(data)
    gen_plot_iterate(data, inDir / file)
    plt.savefig(outDir / image, dpi=300)
    plt.clf()

main()