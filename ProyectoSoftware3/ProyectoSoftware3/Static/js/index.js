$(function () {

    $("#btnIngresar").button().click(function () {


        var usuario = $("#usuario").val();
        var clave = $("#password").val();
        if (usuario == "" || clave == "")
        {
            $("#aviso").text("Campos incompletos");
        } else
        {
            $.ajax({
                data: {'usuario': usuario, 'clave': clave},
                url: 'Login/',
                type: 'GET',
                dataType: "json",
                success: function (data)
                {
                    console.log(data)
                    console.log(data.respuesta);
                    if (data.respuesta == "existe")
                    {
                        $("#aviso").text("Exito");
                        window.location="/Proyeccion/Docente/";
                    } else
                    {
                        $("#aviso").text("Usuario o clave erronea");
                    }

                }
            });
        }
    });
});
