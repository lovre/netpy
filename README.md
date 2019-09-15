# NetPy '19: Introduction to Network Analysis in Python

###### Workshop instructor

**Asst. Prof. [Lovro Šubelj](http://lovro.lpt.fri.uni-lj.si), PhD**, University of Ljubljana

###### Workshop schedule

Thursday, **19th September 2019 at 3:30 PM** (4 hours with breaks)

###### Workshop location

**Lecture room 3 at [UL FRI](http://www.fri.uni-lj.si)**, Večna pot 113, Ljubljana

###### Materials and forum

+ **GitHub** repository at [**http://github.com/lovre/netpy**](http://github.com/lovre/netpy)
+ **WWW** repository at [**http://lovro.lpt.fri.uni-lj.si/netpy**](http://lovro.lpt.fri.uni-lj.si/netpy)
+ **Piazza** forum at [**http://piazza.com/fri.uni-lj.si/fall2019/netpy**](http://piazza.com/fri.uni-lj.si/fall2019/netpy)
+ **Slovenian** dictionary at [**http://lovro.lpt.fri.uni-lj.si/netpy/dict.pdf**](http://lovro.lpt.fri.uni-lj.si/netpy/dict.pdf)

###### High-level description

**The workshop is primarily aimed at Python programmers, either academics, professionals or students, that wish to learn the basics of modern network science and practical analyses of complex real networks, such as social, information and biological networks.** Familiarity with the basics of probability theory, statistics and linear algebra is strongly encouraged.
The workshop is based on the Masters level course [**Introduction to Network Analysis**](http://lovro.lpt.fri.uni-lj.si/posters/frinets.pdf) offered at UL FRI.

###### Recommended prerequisites

**It is recommended that attendees bring a laptop with a working installation of [Python](http://www.python.org), and the [NetworkX](http://networkx.github.io) and [CDlib](http://cdlib.readthedocs.io) packages. Alternatively, you can work with any other network analysis package such as [igraph](http://igraph.org), [graph-tool](http://graph-tool.skewed.de) or [SNAP.py](http://snap.stanford.edu/snappy/).** Finally, for the purposes of visualization of smaller networks, it is recommended to have a working installation of some network analysis software such as [Gephi](http://gephi.org) or [visone](http://visone.info).

###### Tentative syllabus

+ **Challenge**: Warmup Guimera's four knights challenge (10 min)
1. From classical graph theory to **modern network science** (30 min)
2. **Large-scale structure** of real networks and graph **models** (50 min)
3. Measures of **node importance** and link analysis **algorithms** (50 min)
4. Network **community**, **core-periphery** and **equivalence** structure (50 min)
5. Network-based **mining**, **visualization** and practical **applications** (50 min)

+ **Hands-on**: Abstraction, centrality, clusters, mining and visualization (~ min)

## Let's start with Guimera's four knights challenge

###### Tentative duration

**5+5 min**

###### Challenge description

To be **revealed in class** =)

![4knights](figs/4knights.png)

## 1. Classical graph theory → modern network science

###### Tentative duration

**15+15 min**

###### Brief description

**Introduction** of networks and selected **motivational examples**. From **classical graph theory** to social network analysis and **modern network science**. Network perspectives in different **fields of science**.

![transportation](figs/transportation.png)

###### Lecture slides

+ [**Networks introduction and motivational examples**](http://lovro.lpt.fri.uni-lj.si/netpy/intro.pdf)
+ [**Brief historical development of network science**](http://lovro.lpt.fri.uni-lj.si/netpy/history.pdf)
+ [**Network perspectives through science**](http://lovro.lpt.fri.uni-lj.si/netpy/perspects.pdf) (tentative)

###### Book chapters

+ Ch. 1: [Introduction](http://networksciencebook.com/chapter/1) in Barabási, A.-L., [_Network Science_](http://networksciencebook.com) (Cambridge University Press, 2016).
+ Ch. 1-5: Introduction etc. in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 1: [Overview](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch01.pdf) in Easley, D. & Kleinberg, J., [_Networks, Crowds, and Markets_](https://www.cs.cornell.edu/home/kleinber/networks-book/) (Cambridge University Press, 2010).

###### Selected must-reads

+ Barabási, A.-L., The network takeover, _Nat. Phys._ **8**(1), 14-16 (2012).
+ Motter, A.E. & Yang, Y., The unfolding and control of network cascades, _Phys. Today_ **70**(1), 33-39 (2017).
+ Cramer, C., Porter, M.A. et al., [_Network Literacy: Essential Concepts and Core Ideas_](https://sites.google.com/a/binghamton.edu/netscied/Network-Literacy-low-res.pdf?attredirects=0) (Creative Commons Licence, 2015).

###### Selected papers

+ Newman, M.E.J., The physics of networks, _Phys. Today_ **61**(11), 33-38 (2008).
+ Cimini, G., Squartini, T. et al., [The statistical physics of real-world networks](https://arxiv.org/abs/1810.05095), _Nat. Rev. Phys._ **1**(1), 58-71 (2019).
+ Newman, M.E.J., Communities, modules and large-scale structure in networks, _Nat. Phys._ **8**(1), 25-31 (2012).
+ Vespignani, A., Modelling dynamical processes in complex socio-technical systems, _Nat. Phys._ **8**(1), 32-39 (2012).
+ Hegeman, T. & Iosup, A., [Survey of graph analysis applications](https://arxiv.org/abs/1807.00382), e-print _arXiv:180700382v1_, pp. 23 (2018).
+ Hidalgo, C.A., Disconnected, fragmented, or united? A trans-disciplinary review of network science, _Appl. Netw. Sci._ **1**, 6 (2016).

## 2. Large-scale network structure and graph models

###### Tentative duration

**30+20 min**

###### Brief description

**TODO**

![smallworld](figs/smallworld.png)

###### Lecture slides

**TODO**

###### Hands-on analysis

**TODO**

###### Book chapters

**TODO**

###### Selected must-reads

**TODO**

###### Selected papers

**TODO**

## 3. Measures of node importance and link analysis

###### Tentative duration

**30+20 min**

###### Brief description

**Node importance** and **measures of centrality**, i.e. clustering coefficients, spectral, closeness and betweenness centrality, and link analysis algorithms. **Link importance** and **measures of bridging**, i.e. betweenness centrality, embeddedness and topological overlap.

![centrality](figs/centrality.png)

###### Lecture slides

+ [**Node importance and measures of centrality**](http://lovro.lpt.fri.uni-lj.si/netpy/centrality.pdf)
+ [**Link analysis for web page importance**](http://lovro.lpt.fri.uni-lj.si/netpy/analysis.pdf) (tentative)
+ [**Link importance and measures of bridging**](http://lovro.lpt.fri.uni-lj.si/netpy/bridging.pdf) (tentative)

###### Hands-on analysis

+ [**Hands-on analysis**](http://lovro.lpt.fri.uni-lj.si/netpy/imdb.pdf) of IMDb actors collaboration network
+ [**IMDb actors collaboration network**](http://lovro.lpt.fri.uni-lj.si/netpy/imdb.net) in Pajek format etc.
+ [**Python script**](http://lovro.lpt.fri.uni-lj.si/netpy/imdb-starter.py) for IMDb actors collaboration network

###### Book chapters

+ Ch. 7: Measures and metrics in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 14: [Link analysis and Web search](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch14.pdf) in Easley, D. & Kleinberg, J., [_Networks, Crowds, and Markets_](https://www.cs.cornell.edu/home/kleinber/networks-book/) (Cambridge University Press, 2010).
+ Ch. 14-15: Classical node centrality etc. in Estrada, E. & Knight, P.A., [_A First Course in Network Theory_](https://global.oup.com/academic/product/a-first-course-in-network-theory-9780198726463?cc=si&lang=en&) (Oxford University Press, 2015).

###### Selected must-reads

+ Jeong, H., Mason, S.P. et al., Lethality and centrality in protein networks, _Nature_ **411**, 41-42 (2001).
+ Jensen, P., Morini, M. et al., [Detecting global bridges in networks](https://arxiv.org/abs/1509.08295), _J. Complex Netw._ **4**(3), 319-329 (2015).
+ Tong, H., Faloutsos, C. & Pan, J.-Y., Fast random walk with restart and its applications, In: _Proceedings of ICDM ’06_ (Washington, DC, USA, 2006), pp. 613-622.

###### Selected papers

+ Freeman, L., A set of measures of centrality based on betweenness, _Sociometry_ **40**(1), 35-41 (1977).
+ Bonacich, P., Power and centrality: A family of measures, _Am. J. Sociology_ **92**(5), 1170-1182 (1987).
+ Kleinberg, J., Authoritative sources in a hyperlinked environment, _J. ACM_ **46**(5), 604-632 (1999).
+ Franceschet, M. & Bozzo, E., [A theory on power in networks](https://arxiv.org/abs/1510.08332), e-print _arXiv:1510.08332v2_, pp. 19 (2016).
+ Everett, M.G. & Valente, T.W., Bridging, brokerage and betweenness, _Soc. Networks_ **44**, 202-208 (2016).
+ Berkhin, P., A survey on PageRank computing, _Internet Math._ **2**(1), 73-120 (2005).

## 4. Clusters of nodes and network mesoscopic structure

###### Tentative duration

**30+20 min**

###### Brief description

**TODO**

![community](figs/community.png)

###### Lecture slides

**TODO**

###### Hands-on analysis

**TODO**

###### Book chapters

**TODO**

###### Selected must-reads

**TODO**

###### Selected papers

**TODO**

## 5. Network-based mining, visualization and applications

###### Tentative duration

**30+20 min**

###### Brief description

**TODO**

![collisions](figs/collisions.png)

###### Lecture slides

**TODO**

###### Hands-on analysis

**TODO**

###### Book chapters

**TODO**

###### Selected must-reads

**TODO**

###### Selected papers

**TODO**