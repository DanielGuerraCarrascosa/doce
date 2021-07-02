//------------------------------------
// - - - - Click Iniciar Sessión - - - 
//------------------------------------
$(document).on("click","#btn-acceso",function(){
	var core = require('acceso');
    var QWeb = core.qweb;
    var rendered_html = QWeb.render('acceso.cuenta_recuperada_portalfarma',{});
});

$(document).on("click","#img-logo_in",function(){
	$("#btn-acceso").hide();
});

$(document).on("click","#prueba",function(){
	location.replace("https://danielguerracarrascosa-doce-user-comprobar-2810110.dev.odoo.com/acceso_desde_portalfarma_ok");
});
