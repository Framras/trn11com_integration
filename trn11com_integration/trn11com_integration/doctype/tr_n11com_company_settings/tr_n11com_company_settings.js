// Copyright (c) 2019, Framras AS-Izmir and contributors
// For license information, please see license.txt

frappe.ui.form.on('TR n11com Company Settings', {
	// refresh: function(frm) {

	// }
		test_integration: function(frm){
	    if(frm.doc.appkey!="" && frm.doc.appsecret!=""){
	        frappe.call({
	            method: "trn11com_integration.api.test_integration",
	            args:{
	                testappkey: frm.doc.appkey,
                    testappsecret: frm.doc.appsecret
	            },
	            callback: function(r){
                    frm.set_value("integrationresult", r.message)
	            }
	        })
	    }
	}
});

