��    9      �  O   �      �  �   �  )   �     �     �     �     �  �  
     �	     �	     
  	   
     &
  
   .
  
   9
     D
  .   I
     x
     �
     �
     �
  	   �
     �
  /   �
  |   �
     Z     f     x     �     �     �     �     �     �     �     �  C   �  	             ,     :     T     [  
   u     �     �     �     �     �     �     �       
          R   *  0   }     �  K  �  �     )   �     �                    4     F     \     m  
   ~     �  	   �  	   �     �  5   �     �     �     �       	          ;     �   U     �     �          '     :     M     V     [     a     h     k  D   s     �     �     �     �     �     �          &     :     ?     S     b     x     �     �     �     �  R   �  1   !     S            3               
      %   5   8   #      6       )                  ,       	             .          0   +                          7   /                          &      "      !          '             9          -   1            *   $      4       (                   2        * The 'Draft' status is used when the Timesheet Document is created.

                             * The 'Confermed' when Timesheet document is ready to be delivered to the customer
 ${object.timesheet_customer_id.name|safe} <b>Customer:</b> <b>Date:</b> <b>Number:</b> <b>Reference:</b> <div style = "font-family: 'Lucica Grande', Ubuntu, Arial, Verdana, sans-serif; font-size: 12px; color: rgb (34, 34, 34); background-color: rgb (255, 255 , 255); ">
                                        <p> Dear Customer $ {object.timesheet_reference_id.name}, </ p>
                                        <p> We attach the intervention report for the technical assistance provided. </ p>
                                        <p> We kindly ask you to read it and return it countersigned for acceptance. </ p>
                                        <p> In case of non-delivery within 5 working days from the date of entry, it will be considered accepted. </ p>
                                        <br/>
                                        <br/>
                                        <p> For any clarification or further information please contact us </ p>
                                        <br/>
                                        <p> Best regards </ p>
             Analytic Line Codice Documento Codice Timesheet Confermed Confirm Created by Created on Date Date of the last message posted on the record. Description Display Name Draft Duration Followers ID If checked new messages require your attention. If this document is not returned countersigned within 5 working days from its date of entry, it will be considered accepted. Is Follower Last Message Date Last Modified on Last Updated by Last Updated on Messages Note Note: Order Out Partner RapportoIntervento${(object.timesheet_date or '').replace('/','_')} Reference Reset To Draft Send by Email Signature  ______________ Status TIMESHEET REPORT DOCUMENT Time spent Timesheet Activities Timesheet Date Timesheet Document Timesheet Name Timesheet Reference Timesheet timesheet line Timesheet total To Customer Total time Unread Messages You cannot confirm a timesheet that have line already refereed line id: %r Ref: %r You cannot confirm a timesheet that have no line timesheet.document Project-Id-Version: Odoo Server 10.0-20180312
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2018-03-16 17:03+0000
PO-Revision-Date: 2018-03-16 18:05+0100
Last-Translator: <>
Language-Team: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: 
Language: it
X-Generator: Poedit 1.8.11
  * Lo stato 'Draft' e' utilizzato quando il  Timesheet Document viene generato.

                             *  'Confermed' quando Timesheet document pronto per essere inviato al cliente
 ${object.timesheet_customer_id.name|safe} <b>Cliente:</b> <b>Data:</b> <b>Numero:</b> <b>Riferimento:</b> <div style="font-family: 'Lucica Grande', Ubuntu, Arial, Verdana, sans-serif; font-size: 12px; color: rgb(34, 34, 34); background-color: rgb(255, 255, 255); ">
                                        <p>Gentile Cliente ${object.timesheet_reference_id.name},</p>
                                        <p>Alleghiamo il rapporto di intervento per l'assistenza tecnica fornita.</p>
                                        <p>Vi chiediamo gentilmente di leggerlo e tornarcelo controfirmato per accettazione.</p>
                                        <p>In caso di mancato recapito entro 5 giorni lavorativi dalla data di immisione, verra' considerato accettato.</p>   
                                        <br/>
                                        <br/>
                                        <p>Per qualsiasi chiarimento o ulteriore informazione non esitate a contattarci</p> 
                                        <br/>                                   
                                        <p>Cordiali Saluti</p>
             Linea conto analitico Codice Documento Codice Timesheet Confermato Conferma Creato da Creato il Data Data dell'ultimo messaggio postato per questo record. Descrizione Nome Visualizzato Draft Durata Followers ID Se selezionato, nuovi messaggi richiedono la tua attenzione In caso il presente documento non venga riconsegnato controfirmato entro 5 giorni lavorativi dalla sua data di immisione, verra' considerato accettato. È Follower Data Ultimo Messaggio Data di ultima modifica Ultima modifica di Ultima modifica il Messaggi Nota Note: Ordine PC Cliente RapportoIntervento ${(object.timesheet_date or '').replace('/','_')} Riferimento Porta a Draft Invia per Email Firma  ______________ Stato RAPPORTO DI INTERVENTO Tempo Utilizzato Attività timesheet Data Timesheet Documento Timesheet Nome Timesheet Riferimento Timesheet timesheet line Timesheet Totale To Customer Tempo totale Messaggi non letti You cannot confirm a timesheet that have line already refereed line id: %r Ref: %r Non puoi confermare un timesheet che non ha linee timesheet.document 