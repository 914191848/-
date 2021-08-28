from ditie_info import target_zhan
from getHtml import get_random_proxy, getHtml, get_source
from bs4 import BeautifulSoup
import json
from house_detail_list import house_detail_list
import random

source = BeautifulSoup(html)
txt = source.text
while '\n\n' in txt:
    txt.replace('\n\n','\n').replace('\t\t','\t').replace('  ',' ')

print(txt)
html = '''	<div class="fangping-tab">
                    <p id="rule2" gio-trace="tracegio_bi" gioEventId="esfdetailtrafficclick" gioJson={"module_var":"经纪人房评","buttonname_var":"最新","vr_var":"是","houseid_var":"501487594"} class="current">最新</p>
            <p id="rule1" gio-trace="tracegio_bi" gioEventId="esfdetailtrafficclick" gioJson={"module_var":"经纪人房评","buttonname_var":"带看最多","vr_var":"是","houseid_var":"501487594"}>带看最多</p>
            	</div>
	<div class="fangping-con-box">

		<div class="fangping-con">
			<div class="fangpinfo">
	            	                    <ul class="fptiao clear">
	                        <li class="fptoux fl">
                                <a td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人" tdJson={"location":"1","houseid":"501487594","type":"最新"} href="/jingjiren/265341.html"  target="_blank"><img  src="https://image.5i5j.com/picture/265341.jpg" onerror="brokerError(this)" alt="我爱我家经纪人徐飞"/></a>
                            </li>
	                        <li class="fpcont fl">
	                            <div class="fptit">
	                                <h2>
	                                	<a td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人" tdJson={"location":"1","houseid":"501487594","type":"最新"} href="/jingjiren/265341.html"  target="_blank">                                        徐飞
                                        </a>
                                    </h2>
																		<label gio-trace="tracegio_bi" gioEventId="onlineconsult" gioJson={"module_var":"经纪人房评","iconlocation_var":"1","agentid_var":"265341"} td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人爱聊" tdJson={"location":"1"} class="ailbtn  skip-login " onclick="sendPrivateCard(265341)" onmousedown="ga('send','event','PC_BJ_二手房源详情页','爱聊按钮','PC_BJ_二手房源详情页_爱聊按钮');"><i></i>在线咨询</label>
									<label gio-trace="tracegio_bi" gioEventId="telconsult" gioJson={"module_var":"经纪人房评","iconlocation_var":"1","agentid_var":"265341","telnum_var":"4008897257转3917"}  class="phbtn pf_broker" data-brokerid="265341" data-mobile="4008897257转3917"><i></i>拨打电话
																				<div class="codesty fp_code hide">
											<img src="" id="pf_broker265341"/>
											<span class="left_jticon"></span>
											<p class="wxtxt">微信扫码打电话</p>
											<p class="wxnote">扫码失败可拨打</p>
											<p class="dhma">4008897257转3917</p>
										</div>
																			</label>

	                                <p td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人爱聊" tdJson={"location":"1","houseid":"501487594","type":"最新"} class="daikan">
										最新带看：2021.08.26										（共带看过1次）</p>
	                                <!--<label>18910977150</label>-->
	                                <label>
                                  		                                    </label>
	                            </div>

	                            <div class="fpneirong">我是北京我爱我家经纪人徐飞，来自河北省石家庄市，二手房手续流程清晰，擅长匹配房源和恰谈。秉承现代房产经纪人准则，用专业、乐观态度和真诚理念，帮您找到合适的家!。本房我带客户实地看过，房子商品房满五年唯一，主卧朝南，次卧室厨房朝南，诚心出售，随时签约。业主自还，没有户口，您有其他房产问题或者实际看房，您可以点击我头像旁边的[咨询]即可与我取得联系，期待您的咨询!。</div>
	                        </li>
	                    </ul>
	                    	                    <ul class="fptiao clear">
	                        <li class="fptoux fl">
                                <a td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人" tdJson={"location":"2","houseid":"501487594","type":"最新"} href="/jingjiren/639846.html"  target="_blank"><img  src="https://image.5i5j.com/picture/639846.jpg" onerror="brokerError(this)" alt="我爱我家经纪人冯世斌"/></a>
                            </li>
	                        <li class="fpcont fl">
	                            <div class="fptit">
	                                <h2>
	                                	<a td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人" tdJson={"location":"2","houseid":"501487594","type":"最新"} href="/jingjiren/639846.html"  target="_blank">                                        冯世斌
                                        </a>
                                    </h2>
																		<label gio-trace="tracegio_bi" gioEventId="onlineconsult" gioJson={"module_var":"经纪人房评","iconlocation_var":"2","agentid_var":"639846"} td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人爱聊" tdJson={"location":"2"} class="ailbtn  skip-login " onclick="sendPrivateCard(639846)" onmousedown="ga('send','event','PC_BJ_二手房源详情页','爱聊按钮','PC_BJ_二手房源详情页_爱聊按钮');"><i></i>在线咨询</label>
									<label gio-trace="tracegio_bi" gioEventId="telconsult" gioJson={"module_var":"经纪人房评","iconlocation_var":"2","agentid_var":"639846","telnum_var":"4008897152转1995"}  class="phbtn pf_broker" data-brokerid="639846" data-mobile="4008897152转1995"><i></i>拨打电话
																				<div class="codesty fp_code hide">
											<img src="" id="pf_broker639846"/>
											<span class="left_jticon"></span>
											<p class="wxtxt">微信扫码打电话</p>
											<p class="wxnote">扫码失败可拨打</p>
											<p class="dhma">4008897152转1995</p>
										</div>
																			</label>

	                                <p td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人爱聊" tdJson={"location":"2","houseid":"501487594","type":"最新"} class="daikan">
										最新带看：2021.08.24										（共带看过1次）</p>
	                                <!--<label>18601376097</label>-->
	                                <label>
                                  		                                    </label>
	                            </div>

	                            <div class="fpneirong">您好,我是我爱我家洋北旗舰店资深买卖经纪人冯世斌,精耕洋桥、西罗园、角门社区6年时间了,熟悉小区的各种户型优缺点，对商业贷款,公积金,组合贷,连环单的街接有着丰富的经验,“责任 诚实 信任 忠诚”是我的服务宗旨。严格要求自己把控交易每一个流程,让客户跟业主放心踏实,期待为您服务!。本房是一套正规的两居室，朝东向，厨卫全明，户型方正无浪费面积，小区中间不临街，满五年唯一，电梯高层视野采光好。。</div>
	                        </li>
	                    </ul>
	                    	                    <ul class="fptiao clear">
	                        <li class="fptoux fl">
                                <a td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人" tdJson={"location":"3","houseid":"501487594","type":"最新"} href="/jingjiren/582676.html"  target="_blank"><img  src="https://image.5i5j.com/picture/582676.jpg" onerror="brokerError(this)" alt="我爱我家经纪人刘帅"/></a>
                            </li>
	                        <li class="fpcont fl">
	                            <div class="fptit">
	                                <h2>
	                                	<a td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人" tdJson={"location":"3","houseid":"501487594","type":"最新"} href="/jingjiren/582676.html"  target="_blank">                                        刘帅
                                        </a>
                                    </h2>
																		<label gio-trace="tracegio_bi" gioEventId="onlineconsult" gioJson={"module_var":"经纪人房评","iconlocation_var":"3","agentid_var":"582676"} td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人爱聊" tdJson={"location":"3"} class="ailbtn  skip-login " onclick="sendPrivateCard(582676)" onmousedown="ga('send','event','PC_BJ_二手房源详情页','爱聊按钮','PC_BJ_二手房源详情页_爱聊按钮');"><i></i>在线咨询</label>
									<label gio-trace="tracegio_bi" gioEventId="telconsult" gioJson={"module_var":"经纪人房评","iconlocation_var":"3","agentid_var":"582676","telnum_var":"4008897152转4068"}  class="phbtn pf_broker" data-brokerid="582676" data-mobile="4008897152转4068"><i></i>拨打电话
																				<div class="codesty fp_code hide">
											<img src="" id="pf_broker582676"/>
											<span class="left_jticon"></span>
											<p class="wxtxt">微信扫码打电话</p>
											<p class="wxnote">扫码失败可拨打</p>
											<p class="dhma">4008897152转4068</p>
										</div>
																			</label>

	                                <p td-trace="tracetd_bi" tdEventId="二手房_详情页_房评经纪人爱聊" tdJson={"location":"3","houseid":"501487594","type":"最新"} class="daikan">
										最新带看：2021.08.23										（共带看过1次）</p>
	                                <!--<label>13691455502</label>-->
	                                <label>
                                  		                                    </label>
	                            </div>

	                            <div class="fpneirong">您好，感谢您在百忙之中游览我的房评!我是我爱我家刘帅，入职我爱我家9年左右时间，一直负责洋桥商圈，对本商圈每个小区，每种户型都特别了解，曾一度获得带看达人、签单王。。采光没遮挡，上下楼方便，中等装修; 商品房满五年唯一，无抵押，有钥匙，看房方便。。小区环境:这个小区周边生活非常便利,物业费低,交通都很便捷。小区内部有生活超市,小区周边就是多路公交车站台。小区边有幼儿园，接孩子也很方便。。您可以点击我头像旁边的[咨询]即可与我取得联系，期待您的咨询!。</div>
	                        </li>
	                    </ul>
	                    			</div>
	        <div class="pageBox fp-page">
	            <div class="pageSty rf"><a href="javascript:void(0);" class="cPage">下一页</a><a href="javascript:void(0);" class="">...</a><a href="javascript:void(0);" class="">3</a><a href="javascript:void(0);" class="">2</a><a href="javascript:void(0);" class="cur">1</a></div>	        </div>
		</div>
	</div>
'''
