//
//  Copyright (c) Microsoft Corporation.
//  Licensed under the MIT license.
//

import SwiftUI

@available(iOS 13.0, macOS 10.15, tvOS 13.0, *)
public extension Image {
    
    /// 使用此初始化器可保持 SVG 矢量特性，放大不失真
    init(fluent: FluentIcon) {
        self.init(fluent.resourceString, bundle: Bundle.module)
        self = self.renderingMode(.template)
    }
}


@available(iOS 13.0, macOS 10.15, tvOS 13.0, *)
#Preview {
    Image(fluent: .bold2User)
        .resizable()
        .frame(width: 400, height: 400)
}
