# main.py
import os
from fastmcp import FastMCP

# 환경 변수(FASTMCP_SERVER_AUTH)를 통해 GoogleProvider가 자동 설정됩니다.
mcp = FastMCP(name="Railway Google OAuth Test")

@mcp.tool
async def get_my_info() -> dict:
    """로그인된 사용자의 정보를 반환합니다."""
    from fastmcp.server.dependencies import get_access_token
    
    # GoogleProvider는 토큰 클레임에 사용자 정보를 담아둡니다.
    token = get_access_token()
    
    return {
        "status": "Authenticated",
        "email": token.claims.get("email"),
        "name": token.claims.get("name"),
        "google_id": token.claims.get("sub")
    }

# Railway나 Docker 환경을 위해 호스트를 0.0.0.0으로 설정
if __name__ == "__main__":
    import uvicorn
    # Railway는 포트를 PORT 환경변수로 주입해줍니다. 없으면 8000 사용.
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="http", host="0.0.0.0", port=port)