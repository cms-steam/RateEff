import os, sys, string, math, ROOT
from ROOT import TFile, TPie, TCanvas, gStyle, gROOT, TPad, TLegend

infile = "/uscms/physics_grp/lpctrig/ingabu/TMD/Silvio/resultsByDS_13TeV_20150122_721_withEff/1.4e+34/hltmenu_13TeV_25ns_combinedRate_correlations_1.4e+34_All_721.root"

savegif = True

f = TFile.Open(infile)

h = f.Get("h_pie_QCD")

pie = TPie(h)

#pie.GetSlice(0).SetFillColor(40)
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

sl1v = pie.GetEntryVal(1)
sl1l = pie.GetEntryLabel(1)
sl2v = pie.GetEntryVal(2)
sl2l = pie.GetEntryLabel(2)
sl3v = pie.GetEntryVal(3)
sl3l = pie.GetEntryLabel(3)
sl4v = pie.GetEntryVal(4)
sl4l = pie.GetEntryLabel(4)
sl5v = pie.GetEntryVal(5)
sl5l = pie.GetEntryLabel(5)
sl6v = pie.GetEntryVal(6)
sl6l = pie.GetEntryLabel(6)
sl7v = pie.GetEntryVal(7)
sl7l = pie.GetEntryLabel(7)
sl8v = pie.GetEntryVal(8)
sl8l = pie.GetEntryLabel(8)
sl9v = pie.GetEntryVal(9)
sl9l = pie.GetEntryLabel(9)
sl10v = pie.GetEntryVal(10)
sl10l = pie.GetEntryLabel(10)
sl11v = pie.GetEntryVal(11)
sl11l = pie.GetEntryLabel(11)
tot = sl1v + sl2v + sl3v + sl4v + sl5v + sl6v + sl7v + sl8v + sl9v + sl10v + sl11v
sl1p = sl1v / tot * 100
sl2p = sl2v / tot * 100
sl3p = sl3v / tot * 100
sl4p = sl4v / tot * 100
sl5p = sl5v / tot * 100
sl6p = sl6v / tot * 100
sl7p = sl7v / tot * 100
sl8p = sl8v / tot * 100
sl9p = sl9v / tot * 100
sl10p = sl10v / tot * 100
sl11p = sl11v / tot * 100


pie.SetEntryLabel(1, "")
pie.SetEntryLabel(2, "")
pie.SetEntryLabel(3, "")
pie.SetEntryLabel(4, "")
pie.SetEntryLabel(5, "")
pie.SetEntryLabel(6, "")
pie.SetEntryLabel(7, "")
pie.SetEntryLabel(8, "")
pie.SetEntryLabel(9, "")
pie.SetEntryLabel(10, "")
pie.SetEntryLabel(11, "")
pie.SetEntryLabel(12, "")
pie.SetEntryLabel(13, "")
pie.SetEntryLabel(14, "")
pie.SetEntryLabel(0, "")

#pie.SetAngularOffset(30.)
#pie.SetRadius(.2)
pie.SetCircle(.27, .5, .24)
#pie.SetLabelFormat("#splitline{%txt}{%val (%perc)}")
#pie.SetLabelFormat("%txt %val (%perc)")
#pie.SetLabelsOffset(.05)

c = TCanvas("cpie", "cpie", 800, 800)
#c.SetLeftMargin(0)

#pie.Draw("3d nol <")
pie.Draw()

#pie.MakeLegend(.55, .55, .95, .85)
leg = TLegend(.55, .25, .95, .75)
leg.AddEntry(pie.GetSlice(1),  sl1l + ' ' + '%1.2f' %sl1v + ' ' + '(%1.2f' %sl1p + '%)', "f")
leg.AddEntry(pie.GetSlice(2),  sl2l + ' ' + '%1.2f' %sl2v + ' ' + '(%1.2f' %sl2p + '%)', "f")
leg.AddEntry(pie.GetSlice(3),  sl3l + ' ' + '%1.2f' %sl3v + ' ' + '(%1.2f' %sl3p + '%)', "f")
leg.AddEntry(pie.GetSlice(4),  sl4l + ' ' + '%1.2f' %sl4v + ' ' + '(%1.2f' %sl4p + '%)', "f")
leg.AddEntry(pie.GetSlice(5),  sl5l + ' ' + '%1.2f' %sl5v + ' ' + '(%1.2f' %sl5p + '%)', "f")
leg.AddEntry(pie.GetSlice(6),  sl6l + ' ' + '%1.2f' %sl6v + ' ' + '(%1.2f' %sl6p + '%)', "f")
leg.AddEntry(pie.GetSlice(7),  sl7l + ' ' + '%1.2f' %sl7v + ' ' + '(%1.2f' %sl7p + '%)', "f")
leg.AddEntry(pie.GetSlice(8),  sl8l + ' ' + '%1.2f' %sl8v + ' ' + '(%1.2f' %sl8p + '%)', "f")
leg.AddEntry(pie.GetSlice(9),  sl9l + ' ' + '%1.2f' %sl9v + ' ' + '(%1.2f' %sl9p + '%)', "f")
leg.AddEntry(pie.GetSlice(10),  sl10l + ' ' + '%1.2f' %sl10v + ' ' + '(%1.2f' %sl10p + '%)', "f")
leg.AddEntry(pie.GetSlice(11),  sl11l + ' ' + '%1.2f' %sl11v + ' ' + '(%1.2f' %sl11p + '%)', "f")

leg.Draw()

la=ROOT.TLatex()
la.SetNDC()
la.SetTextAlign(11)
la.SetTextSize(0.05)

la.SetTextColor(ROOT.kGreen+3) 
xt=.7; yt=.85
la.DrawLatex(xt,yt, "With Filter");
la.DrawLatex(xt,yt-.06, "With 15-30");

c.Update()

outDir="newplots/15to1000wandwoutSilviosCorr/withEff"
if not os.path.exists(outDir):
    os.makedirs(outDir)

outfile=os.path.join(outDir,"piewithfilt15to1000_withEff")

if savegif: 
    plot=outfile + ".gif"
    c.Print(plot)  

raw_input('\npress return to end the program...')
