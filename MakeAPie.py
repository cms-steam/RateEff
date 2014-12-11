import os, sys, string, math, ROOT
from ROOT import TFile, TPie, TCanvas, gStyle, gROOT, TPad

infile = "/uscms/physics_grp/lpctrig/ingabu/TMD/Daniels/resultsByDS_13TeV_20141205_721wPresc_Pie/1.4e+34/hltmenu_13TeV_25ns_combinedRate_correlations_1.4e+34_All_721.root"

savegif = True

f = TFile.Open(infile)

h = f.Get("h_pie_QCD")

pie = TPie(h)

pie.GetSlice(0).SetFillColor(40)
pie.GetSlice(1).SetFillColor(6)
pie.GetSlice(2).SetFillColor(7)
pie.GetSlice(3).SetFillColor(8)
pie.GetSlice(4).SetFillColor(2)
pie.GetSlice(5).SetFillColor(5)
pie.GetSlice(6).SetFillColor(15)
pie.GetSlice(7).SetFillColor(46)
pie.GetSlice(8).SetFillColor(9)
pie.GetSlice(9).SetFillColor(4)
pie.GetSlice(10).SetFillColor(31)
pie.GetSlice(11).SetFillColor(41)


pie.SetAngularOffset(30.)
pie.SetRadius(.24)
pie.SetLabelFormat("#splitline{%txt}{%val (%perc)}")
#pie.SetLabelFormat("%txt %val (%perc)")
#pie.SetLabelsOffset(-.18)

c = TCanvas("cpie", "cpie", 800, 800)
#c.SetLeftMargin(0)

#pie.Draw("3d nol <")
pie.Draw()

c.Update()

outDir="Plots"
if not os.path.exists(outDir):
    os.makedirs(outDir)

outfile=os.path.join(outDir,"pie")

if savegif: 
    plot=outfile + ".gif"
    c.Print(plot)  

raw_input('\npress return to end the program...')
