---
title: "Instantiation of IETF Network Slices in Service Providers Network"
abbrev: "Network models for IETF Network Slice"
category: std

docname: draft-barguil-teas-network-slices-instantation-latest-2
submissiontype: IETF
number:
date:
consensus: true
v: 3
area: "Operations and Management"
workgroup: "OPSAWG"
keyword:
 - Slice Service
 - L3VPN
 - L2VPN

author:
 -
    fullname:  Samier Barguil Giraldo
    organization: Nokia
    role: editor
    email: samier.barguil_giraldo@nokia.com

 -
    fullname: Luis M. Contreras
    organization: Telefonica
    role: editor
    street: Ronda de la Comunicacion, s/n
    city: Madrid
    code: 28050
    country: Spain
    email: luismiguel.contrerasmurillo@telefonica.com
    uri: http://lmcontreras.com

 -
    fullname: Victor Lopez
    organization: Nokia
    email: victor.lopez@nokia.com

 -
    fullname: Reza Rokui
    organization: Ciena
    email: reza.rokui@nokia.com

 -
    fullname: Oscar Gonzalez de Dios
    organization: Telefonica
    email: oscar.gonzalezdedios@telefonica.com

 -
    fullname: Daniel King
    organization: Olddog Consulting
    email: daniel@olddog.co.uk

normative:

informative:


--- abstract

Network Slicing (NS) is an integral part of Service Provider networks.

The IETF has produced several YANG data models to support the
Software-Defined Networking and network slice architecture and
YANG-based service models for network slice (NS) instantiation.  

This document describes the relationship between IETF Network Slice
models for requesting the IETF Network Slices and (e.g., Layer-3 
Service Model, Layer-2 Service Model) and Network Models (e.g., Layer-3
Network Model, Layer-2 Network Model) used during their realizations.

In addition, this document describes the communication between the IETF
Network Slice Controller and the network controllers for the
realization of IETF network slices. 

The IETF Network Slice YANG model provides the customer-oriented view of
the network slice.  Thus, once the IETF Network Slice controller
(NSC) receives a request, it needs to map it to accomplish the specific
parameters expected by the network controllers. The network models are
analyzed to satisfy the IETF Network Slice requirements, and the gaps
in existing models are reported. 

The document also provides operational and security considerations when
deploying network slices in Service Provider networks.