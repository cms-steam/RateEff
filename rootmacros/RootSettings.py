###########################################
##
##  Macros to help with making plots
##
###########################################
import ROOT

def SetStyle():

    from ROOT import gROOT, gStyle

    gROOT.Reset()
    # gROOT.SetStyle("tdrStyle");    
    gROOT.SetStyle("MyStyle");    
    gStyle.SetOptLogy(0);
    gStyle.SetPalette(1);
    gStyle.SetOptTitle(0);
    gStyle.SetOptStat(0);
    gStyle.SetPadTopMargin(0.02);
    gStyle.SetPadTickX(1);

    gStyle.SetLabelSize(0.045, "XYZ");
    gStyle.SetLabelSize(0.04, "Y");
    gStyle.SetTitleSize(0.045, "XYZ");

    gROOT.ForceStyle()

    return

def prepPlot(cname,ctitle,wtopx=750,wtopy=20,ww=500,wh=520):

    c = ROOT.TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)
    #print c.GetWindowTopX()
    #print c.GetWindowTopY()
    #print c.GetWw()
    #print c.GetWh()

    bmargin=0.12
    #rmargin=0.05
    rmargin=0.025
    lmargin=0.12
    tmargin=0.05
    
    c.SetBottomMargin(bmargin);
    c.SetRightMargin(rmargin);
    c.SetLeftMargin(lmargin);
    c.SetTopMargin(tmargin);

    c.SetLogy(0);
    c.SetLogx(0);
    ROOT.SetOwnership(c,1 )

    return c

def prep1by2Plot(cname,ctitle,wtopx=900,wtopy=20,ww=540,wh=700):

    c = ROOT.TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)

    bmargin=0.12
    rmargin=0.02
    lmargin=0.15
    tmargin=0.05
    
    c.SetBottomMargin(bmargin);
    c.SetRightMargin(rmargin);
    c.SetLeftMargin(lmargin);
    c.SetTopMargin(tmargin);

    c.SetLogy(0);
    c.SetLogx(0);
    ROOT.SetOwnership(c,1 )

    pad1 = ROOT.TPad("pad1","This is pad1",0.0,.3,1.0,1.0);
    pad2 = ROOT.TPad("pad2","This is pad1",0.0,0.,1.0,0.3);

    pad1.SetTopMargin(0.05);
    pad1.SetBottomMargin(0.01);
    pad2.SetTopMargin(0.014);
    pad2.SetBottomMargin(0.2);

    rmargin=0.012
    pad1.SetRightMargin(rmargin);
    pad2.SetRightMargin(rmargin);

    lmargin=0.12
    pad1.SetLeftMargin(lmargin);
    pad2.SetLeftMargin(lmargin);

    ROOT.SetOwnership(pad1,1 )
    ROOT.SetOwnership(pad2,1 )
    return c,pad1,pad2


def prep2by1Plot(cname,ctitle,wtopx=900,wtopy=20,ww=540,wh=700):

    c = ROOT.TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)

    bmargin=0.12
    rmargin=0.02
    lmargin=0.15
    tmargin=0.05
    
    c.SetBottomMargin(bmargin);
    c.SetRightMargin(rmargin);
    c.SetLeftMargin(lmargin);
    c.SetTopMargin(tmargin);

    c.SetLogy(0);
    c.SetLogx(0);
    ROOT.SetOwnership(c,1 )

    pad1 = ROOT.TPad("pad1","This is pad1",0.0,0.0,0.5,1.0);
    pad2 = ROOT.TPad("pad2","This is pad1",0.5,0.,1.0,1.0);

    pad1.SetTopMargin(0.05);
    pad1.SetBottomMargin(0.12);
    pad2.SetTopMargin(0.05);
    pad2.SetBottomMargin(0.12);

    rmargin=0.02
    pad1.SetRightMargin(rmargin);
    pad2.SetRightMargin(rmargin);

    lmargin=0.12
    pad1.SetLeftMargin(lmargin);
    pad2.SetLeftMargin(lmargin);

    ROOT.SetOwnership(pad1,1 )
    ROOT.SetOwnership(pad2,1 )
    return c,pad1,pad2


def prep2by2Plot(cname,ctitle,wtopx=900,wtopy=20,ww=700,wh=700):

    c = ROOT.TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)

    bmargin=0.12
    rmargin=0.02
    lmargin=0.15
    tmargin=0.05
    
    c.SetBottomMargin(bmargin);
    c.SetRightMargin(rmargin);
    c.SetLeftMargin(lmargin);
    c.SetTopMargin(tmargin);

    c.SetLogy(0);
    c.SetLogx(0);
    ROOT.SetOwnership(c,1 )

    pcol=0  # color of pad

    pads=[]
    pads.append(ROOT.TPad('pad1','This is pad1',0.0,0.5,0.5,1.0,pcol))
    pads.append(ROOT.TPad('pad2','This is pad2',0.5,0.5,1.0,1.0,pcol))
    pads.append(ROOT.TPad('pad3','This is pad3',0.0,0.0,0.5,0.5,pcol))
    pads.append(ROOT.TPad('pad4','This is pad4',0.5,0.0,1.0,0.5,pcol))

    for i in range(len(pads)):
        margin=0.02
        pads[i].SetRightMargin(margin)

        margin=0.15
        pads[i].SetLeftMargin(margin)
        ROOT.SetOwnership(pads[i],1 )


    return c,pads


def PrepLegend(x1,y1,x2,y2,size=0.038,color=ROOT.kWhite):
    
    legend = ROOT.TLegend(x1, y1, x2, y2)

    legend.SetTextSize(size)
    legend.SetFillColor(color)
    legend.SetLineColor(color)
    legend.SetShadowColor(color);

    return legend


def SetHistColorAndMarker(h,color,marker):

    h.SetLineColor(color)
    if marker>0:
        h.SetMarkerStyle(marker)
        h.SetMarkerColor(color)
        
    return

def ResetAxisAndLabelSizes(h,lsize=0.055, loff=0.008):

    ## lsize=0.055, loff=0.008 good for 1x2 plots

    h.SetTitleSize( lsize, "X" ); h.SetTitleOffset(loff, "X");
    h.SetTitleSize( lsize, "Y" ); h.SetTitleOffset(loff, "Y");
    h.SetLabelSize( lsize, "X" ); h.SetLabelOffset(loff, "X");
    h.SetLabelSize( lsize, "Y" ); h.SetLabelOffset(loff, "Y");

def DrawText(xtxt,ytxt,theText,txtsize=0.05,textAlign=11):
    from ROOT import TLatex

    t = TLatex();
    t.SetNDC();

    t.SetTextAlign(textAlign)
    t.SetTextSize(txtsize);
    t.SetTextAlign(textAlign)
    t.DrawLatex(xtxt,ytxt,theText);

    return

def drawErrorBars(c,h,offset):
    from ROOT import TLine

    c.cd()
    nbins=h.GetNbinsX()


    # SetOwnership( leg, 0 )   # 0 = release (not keep), 1 = keep
    c.Modified()
    c.Update()

    for ibin in range(1,nbins+1):

        l=TLine()
        l.SetLineWidth(2)
        ROOT.SetOwnership( l, 0 )
        
        cont=h.GetBinContent(ibin);
        err =h.GetBinError(ibin);
        center=h.GetXaxis().GetBinCenter(ibin)+offset
        print ibin, h.GetXaxis().GetBinLabel(ibin), cont, " +- ", err, " ", center

        l.SetY1(center); l.SetY2(center);
        l.SetX1(cont-err); l.SetX2(cont+err);
        l.Draw()


def drawErrorBarsUser(c,h,i1,i2,offset,minY):
    from ROOT import TLine

    c.cd()
    nbins=h.GetNbinsX()

    # print "XXXXX: ",c.GetUxmin(),c.GetX1(),c.GetXlowNDC(),h.GetMinimum(),h.GetYaxis().GetXmin()

    # SetOwnership( leg, 0 )   # 0 = release (not keep), 1 = keep
    c.Modified()
    c.Update()
    # for ibin in range(1,nbins+1):
    if i2>nbins:
        i2=nbins

    for ibin in range(i1,i2+1):

        l=TLine()
        l.SetLineWidth(2)
        ROOT.SetOwnership( l, 0 )
        
        cont=h.GetBinContent(ibin);
        err =h.GetBinError(ibin);
        center=h.GetXaxis().GetBinCenter(ibin)+offset
        print ibin, h.GetXaxis().GetBinLabel(ibin), cont, " +- ", err, " ", center

        l.SetY1(center); l.SetY2(center);
        l.SetX1(cont-err); l.SetX2(cont+err);
        if abs(cont) > minY:
            l.Draw()

def ZeroErrorBars(histo):

    nbins=histo.GetNbinsX()
    for ibin in range(1,nbins+1):
        histo.SetBinError(ibin,0.)

    return
