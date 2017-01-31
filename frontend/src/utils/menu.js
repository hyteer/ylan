module.exports = [
  {
    key: 'dashboard',
    name: '信息面板',
    icon: 'laptop'
  },
  {
    key: 'users',
    name: '产品管理',
    icon: 'user'
  },
  {
    key: 'ui',
    name: '仓库管理',
    icon: 'camera-o',
    clickable: false,
    child: [
      {
        key: 'ico',
        name: '库存信息'
      },
      {
        key: 'search',
        name: '仓库管理'
      }
    ]
  },
  {
    key: 'navigation',
    name: '历史信息',
    icon: 'setting',
    child: [
      {
        key: 'navigation1',
        name: '二级导航1'
      },
      {
        key: 'navigation2',
        name: '二级导航2',
        child: [
          {
            key: 'navigation21',
            name: '三级导航1'
          },
          {
            key: 'navigation22',
            name: '三级导航2'
          }
        ]
      }
    ]
  }
]
