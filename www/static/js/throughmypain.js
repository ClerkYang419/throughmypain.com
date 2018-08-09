// $(function(){
//     var nav=$('#nav-bar'); //得到导航对象
//     var win=$(window); //得到窗口对象
//     var doc=$(document);//得到document文档对象。
//     win.scroll(function(){
//         'asd'.tr
//       if(doc.scrollTop()>=1){
//         nav.addClass("nav-bar-fixed");
//       }else{
//         nav.removeClass("nav-bar-fixed");
//       }
//     })
// })

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  // document.getElementById("main").style.position = "absolute";
  //  document.getElementById("main").style.left = "250px";
  // document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  // document.getElementById("main").style.position = 'fixed';
  // document.body.style.backgroundColor = "white";
}


