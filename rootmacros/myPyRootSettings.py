from ROOT import TCanvas, SetOwnership, gPad, TPad
# def prepPlot(CanvasName="c1",logy=False):
# 
#     c1 = TCanvas('c1',CanvasName,174, 31, 750, 500)
# 
#     bmargin=0.4
#     rmargin=0.02
#     lmargin=0.075
#     tmargin=0.05
#     
#     c1.SetBottomMargin(bmargin);
#     c1.SetRightMargin(rmargin);
#     c1.SetLeftMargin(lmargin);
#     c1.SetTopMargin(tmargin);
# 
#     if (logy):
#         c1.SetLogy(1);
#     else:
#         c1.SetLogy(0);
#     c1.SetLogx(0);
#     SetOwnership(c1,1 )
#     return c1

def prepPlot(cname,ctitle,wtopx=750,wtopy=20,ww=500,wh=520):

    c = TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)
    #print c.GetWindowTopX()
    #print c.GetWindowTopY()
    #print c.GetWw()
    #print c.GetWh()

    bmargin=0.12
    rmargin=0.05
    lmargin=0.12
    tmargin=0.05
    
    c.SetBottomMargin(bmargin);
    c.SetRightMargin(rmargin);
    c.SetLeftMargin(lmargin);
    c.SetTopMargin(tmargin);

    c.SetLogy(0);
    c.SetLogx(0);
    SetOwnership(c,1 )

    return c

def prep1by2Plot(cname,ctitle,wtopx=900,wtopy=20,ww=540,wh=700):

    c = TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)

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
    SetOwnership(c,1 )

    pad1 = TPad("pad1","This is pad1",0.0,.3,1.0,1.0);
    pad2 = TPad("pad2","This is pad1",0.0,0.,1.0,0.3);

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

    SetOwnership(pad1,1 )
    SetOwnership(pad2,1 )
    return c,pad1,pad2


def prep2by1Plot(cname,ctitle,wtopx=900,wtopy=20,ww=540,wh=700):

    c = TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)

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
    SetOwnership(c,1 )

    pad1 = TPad("pad1","This is pad1",0.0,0.0,0.5,1.0);
    pad2 = TPad("pad2","This is pad1",0.5,0.,1.0,1.0);

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

    SetOwnership(pad1,1 )
    SetOwnership(pad2,1 )
    return c,pad1,pad2


def prep2by2Plot(cname,ctitle,wtopx=900,wtopy=20,ww=700,wh=700):

    c = TCanvas(cname,ctitle,wtopx,wtopy,ww,wh)

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
    SetOwnership(c,1 )

    pcol=0  # color of pad

    pads=[]
    pads.append(TPad('pad1','This is pad1',0.0,0.5,0.5,1.0,pcol))
    pads.append(TPad('pad2','This is pad2',0.5,0.5,1.0,1.0,pcol))
    pads.append(TPad('pad3','This is pad3',0.0,0.0,0.5,0.5,pcol))
    pads.append(TPad('pad4','This is pad4',0.5,0.0,1.0,0.5,pcol))

    for i in range(len(pads)):
        margin=0.02
        pads[i].SetRightMargin(margin)

        margin=0.15
        pads[i].SetLeftMargin(margin)
        SetOwnership(pads[i],1 )


    return c,pads
