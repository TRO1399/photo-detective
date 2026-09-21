import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import io
import streamlit.components.v1 as components

st.set_page_config(page_title="Privacy Photo Detective 2026", layout="centered")
st.title("🕵️‍♂️ Photo Detective & Wiper")
st.write("ระบบสืบพิกัดพร้อมปุ่มลบล้างประวัติติดตามจากไฟล์ภาพถ่ายเพื่อความปลอดภัย 100%")
uploaded_file = st.file_uploader("เลือกไฟล์ภาพถ่าย (JPG, JPEG)...", type=["jpg", "jpeg"])

def get_lat_lon(gps_info):
    lat = gps_info.get(1); lat_ref = gps_info.get(2); lon = gps_info.get(3); lon_ref = gps_info.get(4)
    if lat and lat_ref and lon and lon_ref:
        try:
            lat_dec = float(lat)/float(lat) + float(lat)/float(lat)/60.0 + float(lat)/float(lat)/3600.0 if isinstance(lat, tuple) else float(lat)
            if lat_ref != 'N': lat_dec = -lat_dec
            lon_dec = float(lon)/float(lon) + float(lon)/float(lon)/60.0 + float(lon)/float(lon)/3600.0 if isinstance(lon, tuple) else float(lon)
            if lon_ref != 'E': lon_dec = -lon_dec
            return lat_dec, lon_dec
        except: return None
    return None

if uploaded_file is not None:
    file_bytes = uploaded_file.read(); image = Image.open(io.BytesIO(file_bytes))
    st.image(image, caption="ภาพต้นฉบับที่อัปโหลด", use_container_width=True)
    exif_data = image._getexif()
    if exif_data is None:
        st.warning("⚠️ ไม่พบข้อมูล Metadata (EXIF) หรือพิกัดในภาพถ่ายนี้")
    else:
        st.success("🤖 ถอดรหัสข้อมูลภาพสำเร็จ!"); info_dict = {}; gps_info = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "GPSInfo":
                for gps_tag_id in value: gps_info[gps_tag_id] = value[gps_tag_id]
            else: info_dict[tag] = value
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📱 ข้อมูลตัวเครื่อง")
            st.write(f"**ยี่ห้อกล้อง:** {info_dict.get('Make', 'ไม่ระบุ')}")
            st.write(f"**รุ่นมือถือ:** {info_dict.get('Model', 'ไม่ระบุ')}")
            st.write(f"**วันเวลาที่ถ่าย:** {info_dict.get('DateTime', 'ไม่ระบุ')}")
        with col2:
            st.subheader("🌐 พิกัดดาวเทียม (GPS)")
            coords = get_lat_lon(gps_info)
            if coords:
                lat, lon = coords; st.write(f"**ละติจูด:** `{lat}`"); st.write(f"**ลองจิจูด:** `{lon}`")
                maps_url = f"https://google.com{lat},{lon}"
                st.markdown(f"[📍 คลิกเปิดพิกัดบน Google Maps ของจริง]({maps_url})")
            else: st.write("❌ ภาพนี้ไม่มีการบันทึกพิกัดตำแหน่ง (GPS)")
    st.write("---")
    st.subheader("🧹 โหมดทำความสะอาดไฟล์ลบประวัติติดตาม")
    clean_image = Image.open(io.BytesIO(file_bytes)); data_bytes = io.BytesIO(); clean_image.save(data_bytes, format=image.format)
    st.download_button(label="💾 ดาวน์โหลดรูปภาพที่ลบพิกัดแล้ว (Clean Image)", data=data_bytes.getvalue(), file_name=f"clean_{uploaded_file.name}", mime=f"image/{image.format.lower()}")

# =========================================================================
# 💰 โซนตู้สูบเงินดอลลาร์อัตโนมัติ (Adsterra Integration Zone) 💰
# =========================================================================
st.write("---")
st.caption("🔒 สปอนเซอร์ผู้สนับสนุนระบบคุ้มกันภัยความปลอดภัยไซเบอร์")

# 1. แบนเนอร์ป้ายยาว 728x90 ด้านบน
ad_728_90 = """
<div style="text-align:center;">
<script type="text/javascript">
	atOptions = {
		'key' : 'ae4497a3b2aa3764c8cd454df4da10af',
		'format' : 'iframe',
		'height' : 90,
		'width' : 728,
		'params' : {}
	};
</script>
<script type="text/javascript" src="//://highrevenueformat.com"></script>
</div>
"""
components.html(ad_728_90, height=100)

# 2. ป้ายกล่องสี่เหลี่ยม 300x250 ด้านล่าง
ad_300_250 = """
<div style="text-align:center;">
<script type="text/javascript">
	atOptions = {
		'key' : '85f7a043ab3c82170b5d5e1914d691d1',
		'format' : 'iframe',
		'height' : 250,
		'width' : 300,
		'params' : {}
	};
</script>
<script type="text/javascript" src="//://highrevenueformat.com"></script>
</div>
"""
components.html(ad_300_250, height=260)
