import os, sys, string, math, ROOT
from ROOT import TH1,TAxis,TFile, TPie, TColor,TCanvas, gStyle, gROOT, TPad, TLegend

infile = "RatePerSample/hltmenu_13TeV_25ns_combinedRate_1.4e+34_All_721_withEff.root"

savegif = True
gStyle.SetLegendFont(102)
f = TFile.Open(infile)

h = f.Get("ratepersample")
nbins=h.GetNbinsX()
pie = TPie(h)
colors=[6,TColor.kPink-9,8,2,15,5,46,9,4,7,41,TColor.kRed-9,63,74,TColor.kYellow+2,TColor.kOrange+7,30,TColor.kCyan+3]

slv =[ pie.GetEntryVal(0) ]
sll = [ pie.GetEntryLabel(0)]
sle = [ h.GetBinError(1)]
tot=pie.GetEntryVal(0)
for i in range(1,nbins):
    sle.append(h.GetBinError(i+1))
    slv.append(pie.GetEntryVal(i))
    sll.append(pie.GetEntryLabel(i))
    tot = tot + slv[i]
slp = [slv[0] / tot * 100]
pie.SetEntryLabel(0, "")
for i in range(1,len(slv)):
    pie.GetSlice(i).SetFillColor(colors[i])
    slp.append(slv[i] / tot * 100)
    pie.SetEntryLabel(i, "")

#pie.SetAngularOffset(30.)
#pie.SetRadius(.2)
pie.SetCircle(.27, .5, .24)
#pie.SetLabelFormat("#splitline{%txt}{%val (%perc)}")
#pie.SetLabelFormat("%txt %val (%perc)")
#pie.SetLabelsOffset(.05)

c = TCanvas("cpie", "cpie", 800, 800)

pie.Draw()

#pie.MakeLegend(.55, .55, .95, .85)
leg = TLegend(.55, .25, .95, .75)
leg.SetFillColor(TColor.kWhite)
leg.SetTextSize(0.02)
for i in range(0,len(slv)):
    if slv[i]<1:
        num='{:1.2f}{:2}{:>1.2f}'.format(slv[i],'#pm',sle[i])
    else :
        num='{:1.1f}{:2}{:>1.1f}'.format(slv[i],'#pm',sle[i])
    
    leglis=[sll[i].ljust(18,' '),num.rjust(8,' ')]
    legline='{0[0]:<18}{0[1]:>8}'.format(leglis) 
    leg.AddEntry(pie.GetSlice(i), legline, "f")

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

outfile=os.path.join(outDir,"RPSpiewfilt15to1000_withEff")

if savegif: 
    plot=outfile + ".gif"
    c.Print(plot)  

raw_input('\npress return to end the program...')
