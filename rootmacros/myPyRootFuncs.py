from ROOT import SetOwnership

def DivideHistograms(hNum,hDen,c1=1.,c2=1.,WhichErrors="",newName=""):

    hRat= hNum.Clone()

    if len(newName) == 0:
        hRat.SetName("Ratio")
    else:
        hRat.SetName(newName)

    hRat.Divide(hNum,hDen,c1,c2,WhichErrors);

    return hRat

def DrawText(xtxt,ytxt,leglabel,txtsize=0.05):
    from ROOT import TLatex

    t = TLatex();
    t.SetNDC();

    t.SetTextSize(txtsize);
    t.DrawLatex(xtxt,ytxt,leglabel);

    return

def Proj3D_Z(h,xmin,xmax,ymin,ymax,Debug=False):

    # project 3D histogram into 1D along Z (x and y into Z)

    imin=h.GetXaxis().FindBin(xmin+0.01)
    imax=h.GetXaxis().FindBin(xmax-0.01)

    jmin=h.GetYaxis().FindBin(ymin+0.01)
    jmax=h.GetYaxis().FindBin(ymax-0.01)

    if Debug: 
        n= h.GetXaxis().GetNbins()
        print "X-axis,low edge,upper edge:",\
            h.GetXaxis().GetBinLowEdge(1),h.GetXaxis().GetBinUpEdge(n)
        print "Y-axis,low edge,upper edge:",\
            h.GetYaxis().GetBinLowEdge(1),h.GetYaxis().GetBinUpEdge(n)

        print imin,xmin
        print imax,xmax

        print jmin,ymin
        print jmax,ymax


    hname="projZ_" + str(xmin) + "-" + str(xmax) +"__"+ str(ymin) + "_" + str(ymax)
    proj_z=h.ProjectionZ(hname, imin, imax, jmin, jmax)
    SetOwnership(proj_z,True)

    if Debug:
        n= proj_z.GetXaxis().GetNbins()
        print hname
        print "Proj_z low edge,upper edge:",\
            proj_z.GetXaxis().GetBinLowEdge(1),proj_z.GetXaxis().GetBinUpEdge(n)
        print proj_z.GetEntries()

    return proj_z

class XSFIT:
   def __call__( self, x, par ):
       value = par[0]/x[0]**(par[1])+par[2]/x[0]**(par[3]);
       return value

class GFIT:
   def __call__( self, x, par ):
      # value1 = par[0]*math.exp(-0.5 * (x[0] - par[1])**2 / par[2]**2 );
      # value2 = par[3]*math.exp(-0.5 * (x[0] - par[4])**2 / par[5]**2 );

      value1 = par[0]*math.exp(-0.5 * ((x[0] - par[1])/par[2])**2 );
      value2 = par[3]*math.exp(-0.5 * ((x[0] - par[4])/par[5])**2 );

      return par[6]-(value1+value2)
